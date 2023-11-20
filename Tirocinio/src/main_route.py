import hashlib
import datetime
from src.dbConnection import  utenti, sensori
"from src import login_manager"
from src.model import utente, sensore
from src.load_DB import main_load

from bson.objectid import ObjectId
from datetime import timedelta
from flask import request, render_template, session, jsonify, redirect, url_for
from src import app
from flask_login import current_user, login_required , login_user, logout_user

@app.route("/listaSensori",methods=["GET", "POST"])
def listaSensori():
    user = "655b2d8bc8efd2c7e81c8f7e"
    listaSensori = main_load.RetriveSensori(user)
    
    return render_template("listaSensori.html", listaSensori=listaSensori)

"""
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
            redirectUrl = "abbonati"
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
"""