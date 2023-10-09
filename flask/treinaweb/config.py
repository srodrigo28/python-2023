app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format( 
        SGBD='mysql+mysqlconnector', 
        usuario='root', 
        senha='', 
        servidor='localhost', 
        database='jogoteca2'
)