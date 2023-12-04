import hashlib
import datetime
from src.dbConnection import  utenti, sensori
from src import login_manager
from src.model import utente, sensore
from src import help_functions
from src.load_DB import main_load
from src.Adapters.OpenMeteoAdapter import OpenMeteoAdapter as OpenMeteo

from bson.objectid import ObjectId
from datetime import timedelta
from flask import request, render_template, session, jsonify, redirect, url_for
from src import app
from flask_login import current_user, login_required , login_user, logout_user

@app.route("/listaSensori",methods=["GET", "POST"])
@login_required
def listaSensori():
    user = current_user.id
    listaSensori = main_load.RetriveSensori(user)
    return render_template("listaSensori.html", listaSensori=listaSensori)


@app.route("/login",methods=["GET", "POST"])
def login():
        successo = False
        risposta ={
            "PasswordNonValida" : False,
        }
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            urlLastPage = request.form.get("next")
            redirectUrl = "listaSensori"
            tentativo_login: utente = main_load.UtentebyEmail(email)
            if not tentativo_login:
                        #Utente non Registato
                        successo = False
            if tentativo_login.password == password:
                        login_user(tentativo_login, duration= timedelta(days=365),force=True)
                        successo = True
            else:
                        #Passeord sbagiata 
                        successo = False
                        risposta["PasswordNonValida"] = True
            if successo:
                # Se ha provato ad accedere ad una pagina prima di arrivare al
                # login automaticamente:
                if (urlLastPage):
                    redirectUrl = urlLastPage
                return redirect(redirectUrl)
            else:
                return render_template("login.html", risposta = risposta)
        else:
            return render_template("login.html", risposta = risposta)

@login_manager.user_loader
def load_user(user_id):
        return main_load.UtentebyID(user_id)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/dettagliSensore", methods=["POST", "GET"])
def dettagliSensore():
    idsensore = request.args.get("idsensore")
    sensore = main_load.SensorebyID(idsensore)
    lat = sensore.loc['geometry']['coordinates'][0]
    lon = sensore.loc['geometry']['coordinates'][1]
    openmeteo = OpenMeteo(lat,lon)
    meteo = openmeteo.get_data()
    return render_template("dettagliSensore.html", sensore=sensore, meteo=meteo)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_pages/404.html'), 404


@app.route("/aggiungiSensore", methods=['GET', 'POST'])
@login_required
def aggiungiSensore():
    if(request.method != "POST"):
        return render_template("aggiungiSensore.html")
    elif request.method == "POST":
        richiesta = request.get_json()
        nome = richiesta.get("nomeSensore")
        posizioneSensore = richiesta.get("posizioneSensore")
        checkboxes = richiesta.get("sensoriselezionati")
        user = current_user.id
        sensoriselezionati = help_functions.creadict(checkboxes)
        control = main_load.AggiungiSensore(nome,None,None,None,user,posizioneSensore,sensoriselezionati)

        if control != None:
            return jsonify({"success": True})
        elif control == None:
            return jsonify({"success": False})