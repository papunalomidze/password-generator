# auth.py

from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not username or not password or not confirm_password:
            error = 'Please fill in all the fields'
            return render_template('auth.html', auth_type='register', error=error)

        if len(password) < 8:
            error = 'Password should be at least 8 characters'
            return render_template('auth.html', auth_type='register', error=error)

        if password != confirm_password:
            error = 'Passwords do not match'
            return render_template('auth.html', auth_type='register', error=error)

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()

        if user:
            error = 'Username already exists'
            conn.close()
            return render_template('auth.html', auth_type='register', error=error)

        hashed_password = generate_password_hash(password, method='sha256')

        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        success = 'Account registered successfully'

        return render_template('auth.html', auth_type='register', success=success) 
    return render_template('auth.html', auth_type='register')

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('generate_pass'))
        else:
            error = 'Invalid username or password'
            return render_template('auth.html', auth_type='login', error=error)

    return render_template('auth.html', auth_type='login')


def register_ge():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not username or not password or not confirm_password:
            error = 'გთხოვთ შეავსოთ ყველა ველი'
            return render_template('auth_ge.html', auth_type='register', error=error)

        if len(password) < 8:
            error = 'პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო'
            return render_template('auth_ge.html', auth_type='register', error=error)

        if password != confirm_password:
            error = 'პაროლები არ ემთხვევა'
            return render_template('auth_ge.html', auth_type='register', error=error)

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()

        if user:
            error = 'მომხმარებელი უკვე არსებობს'
            conn.close()
            return render_template('auth_ge.html', auth_type='register', error=error)

        hashed_password = generate_password_hash(password, method='sha256')

        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        success = 'ანგარიში წარმატებით დარეგისტრირდა'

        return render_template('auth_ge.html', auth_type='register', success=success) 
    return render_template('auth_ge.html', auth_type='register')


def login_ge():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('generate_pass'))
        else:
            error = 'მომხმარებელის სახელი ან პაროლი არასწორია'
            return render_template('auth_ge.html', auth_type='login', error=error)

    return render_template('auth_ge.html', auth_type='login')