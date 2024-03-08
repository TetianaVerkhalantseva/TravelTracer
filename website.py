from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
import secrets
from user import User

from sight.sight import sight
from reglog.reglog import reglog
from user_profile.user_profile import user_profile

import random as rand
from database import  Database
from models.sight import Sight


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "/login"

csrf = CSRFProtect(app)

app.register_blueprint(sight, url_prefix="/sight")
app.register_blueprint(reglog, url_prefix="/reglog")
app.register_blueprint(user_profile, url_prefix="/user-profile")

@loginManager.user_loader
def load_user(email):
    return User.returnObject(email)


@app.route("/")
def index():

    with Database(dict_cursor=True) as db:
        
        sight_model = Sight(db)

        sights = sight_model.getAllSights()

    return render_template("index.html", sights=(rand.sample(sights,3)))

if __name__ == "__main__":
    app.run(debug=True)
