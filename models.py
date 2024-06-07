from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from db import db
from datetime import datetime

class Product(db.Model):
    pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(10))
    cart_items = db.relationship('Cart', back_populates='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.name}>'


class Users(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    cart_items = db.relationship('Cart', back_populates='user', lazy=True)
    
    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return f'<User {self.username}>'
    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.pk'), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('Users', back_populates='cart_items')
    product = db.relationship('Product', back_populates='cart_items')

    def __repr__(self):
        return f'<Cart {self.id}>'