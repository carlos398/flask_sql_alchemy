from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.contacts_route import contacts_route
from config import DATABASE_CONECTION_URI

app = Flask(__name__)

app.secret_key = 'SECRET KEY'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


SQLAlchemy(app)

app.register_blueprint(contacts_route)
