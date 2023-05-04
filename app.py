# app.py

from flask import Flask, render_template, request
from generate import generate
import string

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def generate_password():
    error = None
    password = ''
    if request.method == 'POST':
        length = request.form.get('length')
        if length == '':
            error = 'Please choose a password length.'
        else:
            if int(length) < 8:
                error = 'Your password needs to be a minimum of 8 characters in length.'
            elif int(length) > 50:
                error = 'Your password cannot exceed 50 characters in length.'
            else:
                numbers = 'numbers' in request.form
                alpha_upper = 'alpha_upper' in request.form
                alpha_lower = 'alpha_lower' in request.form
                symbols = 'symbol' in request.form
                if not (numbers or alpha_lower or symbols or alpha_upper):
                    error = 'Please check at least one option.'
                else:
                    password = generate(length, alpha_upper=alpha_upper, alpha_lower=alpha_lower, number=numbers, symbols=symbols)

                    while numbers:
                        if any(char in string.digits for char in password):
                            break 
                        else:
                            password = generate(length, alpha_upper=alpha_upper, alpha_lower=alpha_lower, number=numbers, symbols=symbols)

    return render_template('index.html', password=password, error=error)

@app.route('/geo', methods=['POST', 'GET'])
def georgian():
    error = None
    password = ''
    if request.method == 'POST':
        length = request.form.get('length')
        if length == '':
            error = 'მიუთითეთ პაროლის სიგრძე.'
        else:
            if int(length) < 8:
                error = 'პაროლი შეიძლება იყოს მინიმუმ 8 სიმბოლო.'
            elif int(length) > 50:
                error = 'პაროლი შეიძლება იყოს მაქსიმუმ 50 სიმბოლო.'
            else:
                numbers = 'numbers' in request.form
                alpha_upper = 'alpha_upper' in request.form
                alpha_lower = 'alpha_lower' in request.form
                symbols = 'symbol' in request.form
                if not (numbers or alpha_upper or alpha_lower or symbols):
                    error = 'მონიშმეთ ერთი ან მეტი პარამეტრი.'
                else:
                    password = generate(length, alpha_upper=alpha_upper, alpha_lower=alpha_lower, number=numbers, symbols=symbols)

                    while numbers:
                        if any(char in string.digits for char in password):
                            break 
                        else:
                            password = generate(length, alpha_upper=alpha_upper, alpha_lower=alpha_lower, number=numbers, symbols=symbols)
                    
    return render_template('index_ge.html', password=password, error=error)
