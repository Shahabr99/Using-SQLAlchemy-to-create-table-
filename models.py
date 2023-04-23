from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Person(db.Model):

    __tablename__= 'people'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(20), nullable=False)
    age=db.Column(db.Integer, nullable=True, default=18)
    job=db.Column(db.String(20), nullable=False, )