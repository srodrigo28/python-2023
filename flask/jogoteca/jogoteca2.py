from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola(): 
    lista = ['Tetris', 'Skyrim', 'Crash', 'God Of War', 'Residente Evil 0', 'Residente Evil 2']
    return render_template('lista.html', titulo='Jogos 2023', jogos = lista)

@app.route('/contato')
def contato(): return render_template('contato.html')
    
app.run()