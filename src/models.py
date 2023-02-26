import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites_id = Column(ForeignKey('Favorites.id'))



class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    birth_year = Column(Integer, nullable=True)
    gender = Column(String(250), nullable=True)
    planets_id = Column(ForeignKey('Planets.id'))
    vehicles_id = Column(ForeignKey('Vehicles.id'))


class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    rotation_period = Column(Integer, nullable=True)
    orbital_period = Column(Integer, nullable=True)
    diameter = Column(Integer, nullable=True)
    climate = Column(String(250), nullable=True)
    gravity = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    character_id = Column(ForeignKey('Character.id'))


class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    manufacterer = Column(String(250), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Integer, nullable=True)
    crew = Column(Integer, nullable=True)
    passengers = Column(Integer, nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    character_id = Column(ForeignKey('Character.id'))


class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    favorite_name = Column(String(250), nullable=False)
    user_id = Column(ForeignKey('User.id'))
    character_id = Column(ForeignKey('Character.id'))

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
