from flask import Flask, render_template, request, redirect, url_for
from models import Acao, Session
from monitor import monitorar, calcular_indices_acoes
import subprocess
import os

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
    preco_max = float(request.form['preco_max'])
    session = Session()
    nova_acao = Acao(ticker=ticker, alvo=alvo, preco_max=preco_max)
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
    monitorar()
    return redirect(url_for('index'))

@app.route("/ranking")
def ranking():
    acoes = calcular_indices_acoes()
    return render_template("indices.html", acoes=acoes)

@app.route('/executar_monitor_sub', methods=['POST'])
def executar_monitor_sub():
    script_path = os.path.join(os.path.dirname(__file__), 'monitor.py')
    subprocess.Popen(['python', script_path])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
