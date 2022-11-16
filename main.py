import requests
import json
from flask import Flask

# Установлен интерпретатор версии 3.10 вместо 3.9
# это модуль main.py
# желания что-нибудь изменить в программе НЕТ



def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
 You signed in with another tab or window. Reload to refresh your session.nu1-dz3-VALUTES/main.py at main · AntonMarchenko1956/nu1-dz3-VALUTES
