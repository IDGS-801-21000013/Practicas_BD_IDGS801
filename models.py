from flask_sqlalchemy import SQLAlchemy
import datetime

db=SQLAlchemy()

class Empleados(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    email = db.Column(db.String(50))
    sueldo = db.Column(db.Float)

class Clientes(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    total = db.Column(db.Float)
    fecha = db.Column(db.DateTime)
    dia = db.Column(db.String(20))
    mes = db.Column(db.String(20))