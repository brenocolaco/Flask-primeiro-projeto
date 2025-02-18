from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')

lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos = lista)


@app.route('/novo')
def new():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',]) #por padrão o flask define que as rotas apenas aceitem o metodo GET então devemos definir no methods
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True)