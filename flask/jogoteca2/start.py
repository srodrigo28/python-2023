from flask import Flask, render_template, request, redirect, session, flash, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God Of War 2', 'Rack new Slash', 'PS2')
jogo3 = Jogo('God Of War     3', 'Rack new Slash', 'PS3')
    
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, name, nickname, senha):
        self.nome = name
        self.nickname = nickname
        self.senha = senha
        
usuario1 = Usuario('Bastiao', 'sb', '123')
usuario2 = Usuario('Camila',  'cm', '123')
usuario3 = Usuario('Matheus', 'mt', '123')

usuarios = { usuario1.nickname : usuario1,  
             usuario2.nickname : usuario2,  
             usuario3.nickname : usuario3 }

app = Flask(__name__)
app.secret_key = 'alura'

# db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format( 
        SGBD='mysql+mysqlconnector', 
        usuario='root', 
        senha='', 
        servidor='localhost', 
        database='jogoteca'
    )

db=SQLAlchemy(app)

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name
    
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20), nullable=False)
    nickename = db.Column(db.String(8), nullable=False)
    console = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/jogoteca/lista')
def jogoteca_index(): 
    return render_template('jogoteca/lista.html', titulo='Jogos 2023', jogos = lista)

@app.route('/jogoteca/novo')
def jogoteca_novo(): 
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #return redirect('/jogoteca/login?proxima=novo')
        return redirect(url_for('jogoteca_login', proxima=url_for('jogoteca_novo')))
    return render_template('jogoteca/novo.html')

@app.route('/jogoteca/editar')
def jogoteca_editar(): 
    return render_template('jogoteca/editar.html')

@app.route('/jogoteca/criar', methods=['POST'])
def jogoteca_criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('jogoteca_index'))

@app.route('/jogoteca/login')
def jogoteca_login():
    proxima = request.args.get('proxima')
    return render_template('jogoteca/login.html', proxima=proxima)

@app.route('/jogoteca/autenticar', methods=['POST', ])
def jogoteca_autenticar():
    
    if request.form['usuario'] in usuarios: 
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'Usuário logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Erro usuário ou senha não permetidas')
        return redirect(url_for('jogoteca_login'))

@app.route('/jogoteca/logout')
def logout():
    session['usuario_logado'] = None
    flash('logout efetuado com sucesso!')
    return redirect(url_for('jogoteca_login'))
    
app.run(debug=True)