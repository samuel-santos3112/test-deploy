from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Deployed to Heroku!</h1>"


@app.route('/teste')
def teste():
    return jsonify({"Teste" : "teste"})
