import yfinance as yf
import requests
from models import Acao, Session

TELEGRAM_TOKEN = '6545143551:AAERwgvGGmvVdD2L1N2vKbPkitXbOC9pOng'
CHAT_ID = '1586721273'

def obter_preco(acao):
    ticker = yf.Ticker(acao)
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
        except Exception as e:
            print(f"Erro ao verificar {acao.ticker}: {e}")
    session.close()

if __name__ == '__main__':
    monitorar()
