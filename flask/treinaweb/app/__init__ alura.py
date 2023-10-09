from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format( 
        SGBD='mysql+mysqlconnector', 
        usuario='root', 
        senha='', 
        servidor='localhost', 
        database='jogoteca2'
    )

db=SQLAlchemy(app)
migrate = Migrate(app, db)

from .views import cliente_view
from .models import cliente_model
