from config import db
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_login', __name__)

#Vista inicial de la plataforma (login)
@mod.route("/", methods=["GET", "POST"])
def principal():
    if "usuario" not in session.keys():
        return render_template("/vistas_exteriores/login.html")
    return render_template("home.html")