def create():
    from model import db
 


def data():
    from model import db, User
    db.create_all()
    one = User(name='MaxPayne', password='Azerty123')
    two = User(name='GordonFreeman', password='Qwerty456')
    db.session.add(one)
    db.session.add(two)
    db.session.commit()
    print('SUCCESS')

data()