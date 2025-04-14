from flask import Flask, render_template, request, redirect, url_for
from models import Acao, Session
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    session = Session()
    acoes = session.query(Acao).all()
    session.close()
    return render_template('index.html', acoes=acoes)

@app.route('/add', methods=['POST'])
def add():
    ticker = request.form['ticker'].upper()
    alvo = float(request.form['alvo'])
    session = Session()
    nova_acao = Acao(ticker=ticker, alvo=alvo)
    session.add(nova_acao)
    session.commit()
    session.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:acao_id>')
def delete(acao_id):
    session = Session()
    acao = session.query(Acao).get(acao_id)
    if acao:
        session.delete(acao)
        session.commit()
    session.close()
    return redirect(url_for('index'))

@app.route('/executar_monitor', methods=['POST'])
def executar_monitor():
    subprocess.Popen(['python3', 'monitor.py'])  # Ou 'python' se preferir
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
