from app import db
from model import Users

def data():
    db.create_all()
    one = Users(name='MaxPayne', password='Azerty123')
    two = Users(name='GordonFreeman', password='Qwerty456')
    db.session.add(one)
    db.session.add(two)
    db.session.commit()
    print('SUCCESS')

data()