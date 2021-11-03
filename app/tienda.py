from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User,Cojin
from . import db

tienda = Blueprint('tienda', __name__)



@tienda.route('/ver_cojines',methods=['POST','GET'])
@login_required
def ver_cojines():

    lista_cojines = Cojin.query.all()
    print(lista_cojines)
    return render_template("ver_cojines.html",datos=lista_cojines)