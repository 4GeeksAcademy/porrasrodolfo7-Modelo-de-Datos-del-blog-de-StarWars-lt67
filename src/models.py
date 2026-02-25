from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Usersw (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    apellido: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    personajes_fav: Mapped[List["Personajesfavoritos"]] = relationship(back_populates="usersw")
    planetas_favoritos: Mapped[List["Planetasfavoritos"]] = relationship(back_populates="usersw")
    naves_favoritas: Mapped[List["Navesfavoritas"]] = relationship(back_populates="usersw")


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha": self.fecha,
            # do not serialize the password, its a security breach
        }

class Personajes (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    raza: Mapped[str] = mapped_column(String(120), nullable=False)
    genero: Mapped[str] = mapped_column(String(120), nullable=False)
  
    personajes_favoritos: Mapped[List["Personajesfavoritos"]] = relationship(back_populates="personajes")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "raza": self.raza,
            "genero": self.genero,
            # do not serialize the password, its a security breach
        }    

class Planetas (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    poblacion: Mapped[str] = mapped_column(String(120),  nullable=False)
    terreno: Mapped[str] = mapped_column(String(120),  nullable=False)
  
    planetas_favoritos: Mapped[List["Planetasfavoritos"]] = relationship(back_populates="planetas")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "terreno": self.terreno,
            # do not serialize the password, its a security breach
        }    

class Naves (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    modelo: Mapped[str] = mapped_column(String(120), nullable=False)
    pasajeros: Mapped[int] = mapped_column(Integer)
  
    naves_favoritas: Mapped[List["Navesfavoritas"]] = relationship(back_populates="naves")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "poblacion": self.modelo,
            "pasajeros": self.pasajeros,
            # do not serialize the password, its a security breach
        }    

class Personajesfavoritos(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    usersw_id: Mapped[int] = mapped_column(ForeignKey("usersw.id"))
    usersw: Mapped["Usersw"] = relationship(back_populates="personajes_favoritos")

    personajes_id: Mapped[int] = mapped_column(ForeignKey("personajes.id"))
    personajes: Mapped["Personajes"] = relationship(back_populates="personajes_favoritos")


    def serialize(self):
        return {
            "id": self.id,
            "usersw_id": self.usersw_id,
            "personaje_id": self.personaje_id
            # do not serialize the password, its a security breach
        }
    

class Planetasfavoritos(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    usersw_id: Mapped[int] = mapped_column(ForeignKey("usersw.id"))
    usersw: Mapped["Usersw"] = relationship(back_populates="planetas_favoritos")

    planetas_id: Mapped[int] = mapped_column(ForeignKey("planetas.id"))
    planetas: Mapped["Planetas"] = relationship(back_populates="planetas_favoritos")


    def serialize(self):
        return {
            "id": self.id,
            "usersw_id": self.usersw_id,
            "planetas_id": self.planetas_id
            # do not serialize the password, its a security breach
        }

class Navesfavoritas(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    usersw_id: Mapped[int] = mapped_column(ForeignKey("usersw.id"))
    usersw: Mapped["Usersw"] = relationship(back_populates="naves_favoritas")

    naves_id: Mapped[int] = mapped_column(ForeignKey("naves.id"))
    naves: Mapped["Naves"] = relationship(back_populates="naves_favoritas")


    def serialize(self):
        return {
            "id": self.id,
            "usersw_id": self.usersw_id,
            "naves_id": self.planetas_id
            # do not serialize the password, its a security breach
        }