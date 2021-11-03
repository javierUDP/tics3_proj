from config import db
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_gestion_productos', __name__)

@mod.route("/gestion/productos", methods=["GET"])
def gestion_productos():
    if "usuario" not in session:
        redirect("/")

    return render_template("/productos/gestion_productos.html")

@mod.route("/gestion/productos/cojines", methods=["GET"])
def gestion_cojines():
    if "usuario" not in session:
        redirect("/")

    sql_query = """
        SELECT *
            FROM cojines
    """
    cursor = db.query(sql_query, None)
    lista_cojines = cursor.fetchall()

    sql_query = """
        SELECT caracteristicas_cojin.*, relleno.tipo_relleno
            FROM caracteristicas_cojin, relleno
                WHERE caracteristicas_cojin.id_relleno = relleno.id
    """
    cursor = db.query(sql_query, None)
    caracteristicas = cursor.fetchall()

    sql_query = """
        SELECT *
            FROM relleno
    """
    cursor = db.query(sql_query, None)
    rellenos = cursor.fetchall()

    return render_template("productos/cojines.html",
                            lista_cojines = lista_cojines,
                            caracteristicas = caracteristicas,
                            rellenos = rellenos)

@mod.route("/gestion/productos/cojines/agregar", methods=["POST"])
def añadir_cojin():
    if "usuario" not in session:
        redirect("/")

    data = request.data.form_dict()

    sql_query = """
        INSERT INTO cojines (stock, precio_unitario)
                VALUES (%s, %s)
    """
    db.query(sql_query, (data["stock"], data["price"]))
    sql_query =  """
        INSERT INTO caracteristicas_cojin (id_relleno, altura, ancho, tipo_tela)
                VALUES (%s, %s, %s, %s)
    """
    db.query(sql_query, (data["fill"], data["heigth"], data["width"], data["fabric"]))

    flash("successful-add")
    return redirect(redirect_url())

@mod.route("/gestion/productos/cojines/editar/<string:id_cojin>", methods=["POST"])
def editar_cojin(id_cojin):
    if "usuario" not in session:
        redirect("/")

    data = request.data.form_dict()

    sql_query = """
        UPDATE cojines
            SET (stock, precio_unitario)
                VALUES (%s, %s)
                    WHERE id = %s
    """
    db.query(sql_query, (data["stock"], data["price"], id_cojin))
    sql_query =  """
        UPDATE caracteristicas_cojin
            SET (id_relleno, altura, ancho, tipo_tela)
                VALUES (%s, %s, %s, %s)
                    WHERE id = %s
    """
    db.query(sql_query, (data["fill"], data["heigth"], data["width"], data["fabric"], id_cojin))

    flash("successful-edit")
    return redirect(redirect_url())

@mod.route("/gestion/productos/cojines/eliminar/<string:id_cojin>", methods=["POST"])
def eliminar_cojin(id_cojin):
    if "usuario" not in session:
        redirect("/")

    sql_query = """
        DELETE FROM cojines
            WHERE id = %s
    """
    db.query(sql_query, (id_cojin, ))

    sql_query = """
        DELETE FROM caracteristicas_cojin
            WHERE id = %s
    """
    db.query(sql_query, (id_cojin, ))

    flash("successful-remove")
    return redirect(redirect_url())

