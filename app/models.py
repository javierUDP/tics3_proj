from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Tela(db.Model):
    __tablename__='tela'
    id = db.Column(db.Integer, primary_key=True)
    tipo_tela = db.Column(db.String(64),nullable=False)

    def __repr__(self):
        str = "Id: {}, Tipo_tela: {}\n" 
        str =str.format( self.id, self.tipo_tela)
        return str

class Producto(db.Model):
    __tablename__='productos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(64),nullable=False)
    nombre = db.Column(db.String(64),nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    altura = db.Column(db.String(60), nullable=False)
    ancho = db.Column(db.Float, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    tela_id = db.Column(db.Integer, db.ForeignKey('tela.id'))


    def __repr__(self):
        str = "Id: {}, Nombre: {}, Descripcion: {},Tela_id: {}\n" 
        str =str.format( self.id, self.nombre,self.descripcion,self.tela_id)
        return str

class Compras(db.Model):
    __tablename__='compras'
    id = db.Column(db.Integer, primary_key=True)
    nombre_comprador = db.Column(db.String(64),nullable=True)
    apellido_comprador = db.Column(db.String(64),nullable=True)
    rut = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(60), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    ciudad = db.Column(db.String(30), nullable=True)
    cantidad = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        str = "Id: {}, Nombre Comprador: {}, Descripcion: {}\n" 
        str =str.format( self.id, self.mombre_comprador,self.apellido_comprador)
        return str

