from config import ALLOWED_EXTENSIONS
from datetime import timedelta
from flask import Flask,render_template,request,redirect,url_for,session

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

# Define the WSGI application object
app = Flask(__name__)

# ============================================================================
# Blueprints (Routes)
from app.routes.rutas_home import mod
from app.routes.rutas_gestion_productos import mod
from app.routes.rutas_login import mod

app.register_blueprint(routes.rutas_home.mod)
app.register_blueprint(routes.rutas_login.mod)
app.register_blueprint(routes.rutas_productos.mod)

# Configuraciones adicionales desde config.py
app.config.from_object('config')

# Controlador de errores HTTP
@app.errorhandler(404)
def not_found(error):
    return render_template("/vistas_exteriores/vistas_errores/404_externo.html"), 404

@app.errorhandler(413)
def too_large_request(error):
    return redirect("/")

@app.errorhandler(401)
def not_authorized(error):
    return render_template("/vistas_exteriores/vistas_errores/401_externo.html"), 401

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("/vistas_exteriores/vistas_errores/405_externo.html"), 405

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("/vistas_exteriores/vistas_errores/500_externo.html"), 500

# ------------------------------------------- Filtros Jinja2 para templates
@app.template_filter('nl2br') # Permite cambiar el formato de los saltos de línea en textarea
def nl2br(s):
    if s is None:
        return ""
    s = s.strip()
    s = s.replace("\r","")
    return s.replace("\n", "<br/>")
@app.template_filter('underscore_espacio') # Permite reemplazar espacios por '_'
def underscore_espacio(s):
    return s.replace(" ","_")
# -------------------------------------------

# Timer para sesión activa (Máximo 1 hr inactiva)
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# --------- Funciones útiles ------------------------------------------------

# -------------------------------------------------------------------------------------------