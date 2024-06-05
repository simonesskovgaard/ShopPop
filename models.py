from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from db import db



class Product(db.Model):
    pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(10))


    def __repr__(self):
        return f'<Product {self.name}>'


class Users(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return f'<User {self.username}>'