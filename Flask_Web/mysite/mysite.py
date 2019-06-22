from flask import Flask,abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/great')
@app.route('/great/<name>')
def great(name='goodcat'):
    return '<h1>Hello,%s</h1>' % name

@app.route('/test/<int:year>')
def test(year):
    return '<p>Welcome to %d!</p>' % (2018 - year)


@app.route('/ceshi')
def ceshi():
    return '<h1>Hello,Flask!<h1>',302,{'Location':'http://ip138.com'}

@app.route('/404')
def not_found():
    abort(500)



if __name__ == '__main__':
    app.run()
