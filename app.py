from flask import Flask, session, render_template, redirect,url_for
from auth import register, login, register_ge, login_ge
from generator import generate_password, georgian

app = Flask(__name__)
app.secret_key = 'qwe123123'


@app.route('/')
def home():
    return render_template('auth.html', auth_type='register')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    return register()

@app.route('/login', methods=['GET', 'POST'])
def log():
    return login()

@app.route('/register_ge', methods=['GET', 'POST'])
def reg_ge():
    return register_ge()


@app.route('/login_ge', methods=['GET', 'POST'])
def log_ge():
    return login_ge()


@app.route('/generate', methods=['POST', 'GET'])
def generate_pass():
    return generate_password()

@app.route('/geo', methods=['POST', 'GET'])
def geo():
    return georgian()

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('log'))

if __name__ == '__main__':
    app.run()
