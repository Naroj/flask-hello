from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Marcel'

app.run(host='0.0.0.0', port=10020)
