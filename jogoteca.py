from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def hello():
    lista = ['Tetris', 'Skyrim', 'Crash']
    return render_template('lista.html', titulo='Jogos', jogos = lista)

app.run()