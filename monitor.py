import yfinance as yf
import requests
from models import Acao, Session
from datetime import datetime

TELEGRAM_TOKEN = '6545143551:AAERwgvGGmvVdD2L1N2vKbPkitXbOC9pOng'
CHAT_ID = '1586721273'
LOG_FILE = 'monitor_log.txt'

def log_mensagem(mensagem):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensagem}\n")

def obter_preco(acao):
    ticker = yf.Ticker(f'{acao}.SA')
    preco_atual = ticker.history(period='1d')['Close'].iloc[-1]
    return preco_atual

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, data=data)

def monitorar():
    session = Session()
    acoes = session.query(Acao).all()
    for acao in acoes:
        try:
            preco = obter_preco(acao.ticker)
            if preco <= acao.alvo:
                mensagem = f"🚨 {acao.ticker} atingiu R$ {preco:.2f} (alvo: R$ {acao.alvo:.2f})"
                enviar_telegram(mensagem)
                log_mensagem(mensagem)
        except Exception as e:
            print(f"Erro ao verificar {acao.ticker}: {e}")
    log_mensagem("Sem alvos atingidos")
    session.close()

if __name__ == '__main__':
    monitorar()
