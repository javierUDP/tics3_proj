from config import db
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_home', __name__)

#Vista principal de la plataforma
@mod.route("/home", methods=["GET", "POST"])
def home_principal():
    return render_template("home.html")