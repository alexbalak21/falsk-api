from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

from model import db, User

# INDEX PAGE
@app.route('/')
def home():
    return 'HOME'

#GET ALL USERS
@app.route('/users', methods=['GET'])
def getAll():
    users = User.query.all()
    userslist = []
    for user in users:
        userslist.append(user.toDict())
    return json.dumps(userslist)

# GET 1 USER
@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = User.query.get_or_404(id)
    output = user.toDict()
    return json.dumps(output)

# CREATE USER
@app.route('/newuser',methods=['POST'])
def add_user():
    name = request.json['name']
    password = request.json['password']
    new_user = User(name=name, password=password)
    db.session.add(new_user)
    db.session.commit()
    output = new_user.toDict()
    return json.dumps(output)

# UPDATE USER
@app.route('/user/<id>', methods=['PUT'])
def update(id):
    name = request.json['name']
    password = request.json['password']
    user = User.query.get_or_404(id)
    user.name = name
    user.password = password
    db.session.commit()
    return getUser(id)

# DELETE USER
@app.route('/user/<id>', methods=['DELETE'])
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return 'DELETED'



