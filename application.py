from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, Blueprint
from dotenv import load_dotenv
import os

# Importa o Blueprint do auth.py
from auth import auth

# Carregar as variáveis do arquivo .env
load_dotenv()

application = Flask(__name__)
application.secret_key = os.getenv('SECRET_KEY')
application.register_blueprint(auth, url_prefix='/auth')  # Define um prefixo para as rotas


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/perfil')
def profile():
    return render_template('perfil.html')


@application.route('/termos')
def terms():
    return render_template('termos.html')


@application.route('/politicas')
def polices():
    return render_template('politicas.html')

# Roda o servidor Flask
if __name__ == '__main__':
    application.run(port=5000, debug=True)