from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import psycopg2

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


# PostgreSQL connection setup
conn = psycopg2.connect(
    dbname='shoppop',
    user='shop',
    password='pop',
    host='localhost',
    port=5433
)
db_cursor = conn.cursor()




