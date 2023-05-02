from flask import Flask, render_template, request
from generate import generate

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
            elif int(length) > 100:
                error = 'Your password cannot exceed 100 characters in length.'
            else:
                numbers = 'numbers' in request.form
                alpha = 'alpha' in request.form
                symbols = 'symbol' in request.form
                if not (numbers or alpha or symbols):
                    error = 'Please check at least one option.'
                else:
                    password = generate(length, alpha=alpha, number=numbers, symbols=symbols)
    return render_template('index.html', password=password, error=error)
