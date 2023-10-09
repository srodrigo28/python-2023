from app import db
#from sqlalchemy_utils import ChoiceTypes

class Cliente(db.Model):
    __tablename__ = "clientes"

    # SEXO_CHOICES = [
    #     (u'M', u'Masculino'),
    #     (u'F', u'Feminino'),
    #     (u'N', u'Nenhuma das opções')
    # ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    data_nascimento = db.Column(db.String(30))
    sexo = db.Column(db.String(2))