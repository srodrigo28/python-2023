from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

from .views import cliente_view
