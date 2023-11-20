

from flask import Flask, redirect, render_template, url_for, flash
from flask_login import LoginManager, current_user
from flask_cors import CORS
from flask_pymongo import PyMongo






"""
   This file represents our app, it is from this file that our application starts,
   and it is from this file only that we call all the other modules
   such as routes, or gestioneUtenteControl
"""
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://gerardofrino588:95VOEFttqh89tAsS@cluster0.fdg5slg.mongodb.net/DBTirocinio?retryWrites=true&w=majority"
app.config["COMPRESS_ALGORITHM"] = 'gzip'  # disable default compression of all eligible requests
app.config['SECRET_KEY'] = 'jshwifhjwieoajhf5847f5ae4eaws'
"""
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


from functools import wraps
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.ruolo == "admin":
            return f(*args, **kwargs)
        else:
            msg ="Devi essere un admin per vedere questa pagina."
            return render_template('error_pages/custom_error.html', msg)

    return wrap
""" 

from src import routes
from src import main_route
