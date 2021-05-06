from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from db_Info import db_local

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from rooter import Rooter

root = Rooter()