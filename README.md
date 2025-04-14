# 📈 Monitor de Preço de Ações com Alerta via Telegram

Este é um projeto em Python que monitora o preço de ações específicas da B3 (ex: `PETR4.SA`, `VALE3.SA`) utilizando a API do Yahoo Finance. Quando uma ação atinge o valor alvo definido, você recebe uma notificação via Telegram.

Além disso, o projeto inclui uma interface web em Flask para adicionar/remover ações dinamicamente e armazena os dados em um banco SQLite.

---

## 🚀 Funcionalidades

- ✅ Monitoramento automático de ações da bolsa de valores
- ✅ Alertas via Telegram quando o preço atingir o alvo
- ✅ Interface web para gerenciar as ações
- ✅ Banco de dados SQLite para armazenar os alvos
- ✅ Fácil implantação no PythonAnywhere

---

## 🛠️ Tecnologias

- Python 3.x
- Flask
- yFinance
- SQLite (SQLAlchemy)
- Telegram Bot API
- Schedule

---

## 🖥️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/will-ssilva/stock_target_schedule.git
cd stock_target_schedule
