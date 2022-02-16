import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def mars():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "</br>".join("""Человечество вырастает из детства.\n
    Человечеству мала одна планета.\n
    Мы сделаем обитаемыми безжизненные пока планеты.\n
    И начнем с Марса!\n
    Присоединяйся!""".split("\n"))


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас Марс!</h1>
                    <img src="{flask.url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <h5>Вот она какая, красная планета.</h5>
                  </body>
                </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')