import os
from app import db_wrapper

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ----------------------- Conexión a base de datos MySQL ------------------------------------------------------------
# ---- 00webhost Hosting:
# user="id17879028_admin@2a02:4780:bad:c0de::13", passwd="dj&a9N7-|JvlDaQI", host="localhost",
# port="3306", database="id17879028_tienda_db", autocommit=True

# Conexión a la base de datos mediante wrapper class
db = db_wrapper.DB(user="id17879028_admin@2a02:4780:bad:c0de::13",
                   passwd="dj&a9N7-|JvlDaQI",
                   host="localhost",
                   port="3306",
                   database="id17879028_tienda_db")
# ------------------------------------------------------------------------------------------------------------------
# Configuraciones de archivos
UPLOAD_FOLDER = 'static/upload_folder'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',
                      'xlsx', 'xls', 'csv', 'doc', 'docx', 'ppt',
                      'pptx', 'odp', 'svg'}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = os.urandom(24)

# Secret key for signing cookies
SECRET_KEY = b'7hn/_gth,./;3UUUe4c7_t,2//'