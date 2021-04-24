import os
from os.path import join, dirname

import requests
from dotenv import load_dotenv
from flask import Flask, request

app = Flask(__name__)


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


def send_message(chat_id, text):
    method = "sendMessage"
    token = get_from_env('TELEGRAM_BOT_TOKEN')
    url = f'https://api.telegram.org/bot{token}/{method}'
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route('/', methods=["POST"])
def process():
    chat_id = request.json['message']['chat']['id']
    send_message(chat_id=chat_id, text="test")
    return {"ok": True}


if __name__ == '__main__':
    app.run()
