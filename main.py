from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/name/<value>')
def name(value):
    return f'Hello {value}! I hope you are having a wonderful day!'


@app.route('/bob')
def bob():
    val = {'value': 'bob'}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)