from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

USERNAME = 'root2'
PASSWORD = '2020Admin#.'
SERVER = 'localhost'
DB = 'jogoteca2'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)
migrate = Migrate(app, db)

from .views import cliente_view
from .models import cliente_model
