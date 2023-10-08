from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God Of War 2', 'Rack new Slash', 'PS2')
jogo3 = Jogo('God Of War 3', 'Rack new Slash', 'PS3')
    
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

app.secret_key = 'alura'

@app.route('/')
def index(): 
    return render_template('lista.html', titulo='Jogos 2023', jogos = lista)

@app.route('/novo')
def novo(): return render_template('novo.html')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Usuário logado com sucesso!')
        return redirect('/')
    else:
        flash(session['usuario_logado'] + 'Erro usuário ou senha não permetidas')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('logout efetuado com sucesso!')
    return redirect('/')
    
app.run(debug=True)