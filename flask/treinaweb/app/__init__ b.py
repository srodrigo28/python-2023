from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

USERNAME = 'root'
PASSWORD = ''
SERVER = '127.0.0.1'
DB = 'jogoteca2'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)

from .views import cliente_view
