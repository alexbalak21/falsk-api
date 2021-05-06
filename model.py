from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def toDict(self):
        dic = {"id":self.id, "name":self.name, "password":self.password}
        return dic