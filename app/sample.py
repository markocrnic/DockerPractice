from flask import Flask

app = Flask(__name__)


@app.route('/helloworld/')
def helloworld():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
