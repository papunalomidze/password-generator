from flask import render_template, request
import string
from generate import generate

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
                    while True:
                        password = generate(length, alpha_upper=alpha_upper, alpha_lower=alpha_lower, number=numbers, symbols=symbols)

                        if numbers and not any(char in string.digits for char in password):
                            continue
                        if alpha_upper and not any(char in string.ascii_uppercase for char in password):
                            continue
                        if alpha_lower and not any(char in string.ascii_lowercase for char in password):
                            continue
                        if symbols and not any(char in string.punctuation for char in password):
                            continue

                        break
    return render_template('index.html', password=password, error=error)

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
                    error = 'მონიშნეთ ერთი ან მეტი პარამეტრი.'
                else:
                    while True:
                        password = generate(length, alpha_upper=alpha_upper, alpha_lower=alpha_lower, number=numbers, symbols=symbols)

                        if numbers and not any(char in string.digits for char in password):
                            continue
                        if alpha_upper and not any(char in string.ascii_uppercase for char in password):
                            continue
                        if alpha_lower and not any(char in string.ascii_lowercase for char in password):
                            continue
                        if symbols and not any(char in string.punctuation for char in password):
                            continue

                        break
    return render_template('index_ge.html', password=password, error=error)
