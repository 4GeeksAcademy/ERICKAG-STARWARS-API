from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    favoritos = db.relationship("Favoritos",backref="usuario",lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    height= db.Column(db.String(250), nullable=False)
    gender= db.Column(db.String(250), nullable=False)
    favoritos = db.relationship("Favoritos",backref="character",lazy=True)
        
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    climate= db.Column(db.String(10), nullable=False)
    terrain= db.Column(db.String(10), nullable=False)
    favoritos = db.relationship("Favoritos",backref="planet",lazy=True)
        
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    model= db.Column(db.String(10), nullable=False)
    class_name=db.Column(db.String(10), nullable=False)
    favoritos = db.relationship("Favoritos",backref="vehicle",lazy=True)
        
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuario.id'),nullable=False)
    character_id= db.Column(db.Integer,db.ForeignKey('character.id'),nullable=True)
    planet_id= db.Column(db.Integer, db.ForeignKey('planet.id'),nullable=True)
    vehicle_id= db.Column(db.Integer,db.ForeignKey('vehicle.id'),nullable=True)
        
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario": self.usuario_id,
            "character": self.name,
            "planet": self.character_id,
            # do not serialize the password, its a security breach
        }
