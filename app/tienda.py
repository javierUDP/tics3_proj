from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User,Producto, Compras
from . import db
import datetime

tienda = Blueprint('tienda', __name__)



@tienda.route('/ver_cojines',methods=['POST','GET'])
@login_required
def ver_cojines():
    productos = Producto.query.filter(Producto.tipo.in_([1]))
    print(productos)
    return render_template("ver_cojines.html",productos=productos)

@tienda.route('/producto/<int:cojinid>/')
@login_required
def producto_especifico(cojinid=None):
    producto = Producto.query.filter(Producto.id.in_([cojinid]))
    return render_template("producto_especifico.html", producto = producto)


@tienda.route('/comprar',methods=['POST','GET'])
@login_required
def comprar():
    producto = Producto.query.filter(Producto.id.in_([int(request.form['product_id'])]))
    stock_actual = producto.cantidad
    valor=producto.precio
    cantidad = int(request.form['cantidad'])

    if request.method == 'POST':
        nueva_compra = Compras(
            nombre_comprador = request.form['nombre'],
            apellido_comprador = request.form['apellido'],
            rut = int(request.form['rut']),
        )
        db.session.add(nueva_compra)
        producto_modificado = Producto.query.filter_by(id=int(request.form['id'])).update(dict(stock=stock_actual-int(request.form['cantidad'])))
        db.session.commit()
        return render_template("compra_finalizada.html")

    return render_template("comprar.html",datos=producto,cantidad=cantidad)



#
#@main.route('/ver_cojines',methods=['POST','GET'])
#@login_required
#def ver_cojines():
#	sql = """SELECT * FROM producto, caracteristicas_cojin, relleno, tela WHERE producto.tipo_producto ='%s' AND producto.caracteristicas_id = caracteristicas_cojin.id AND caracteristicas_cojin.id_relleno = relleno.id AND caracteristicas_cojin.id_tela = tela.id;"""%('cojin')
#	cur.execute(sql)
#	lista_cojines = cur.fetchall()
#
#	print(lista_cojines)
#
#	return render_template("ver_cojines.html",datos=lista_cojines)
#