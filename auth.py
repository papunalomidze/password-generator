from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host='papuna.mysql.pythonanywhere-services.com',
            user='papuna',
            password='qwe123123',
            database='papuna$users'
        )
        return conn
    except Error as e:
        print(e)
        return None

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

        conn = create_connection()
        if conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()

            if user:
                error = 'Username already exists'
                conn.close()
                return render_template('auth.html', auth_type='register', error=error)

            hashed_password = generate_password_hash(password, method='sha256')

            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
            conn.commit()
            conn.close()

            success = 'Account registered successfully'

            return render_template('auth.html', auth_type='register', success=success)
        else:
            error = 'Failed to connect to the database'
            return render_template('auth.html', auth_type='register', error=error)
    return render_template('auth.html', auth_type='register')


def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = create_connection()
        if conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()

            conn.close()

            if user and check_password_hash(user[2], password):
                session['username'] = username
                return redirect(url_for('generate_pass'))
            else:
                error = 'Invalid username or password'
                return render_template('auth.html', auth_type='login', error=error)
        else:
            error = 'Failed to connect to the database'
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

        conn = create_connection()
        if conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()

            if user:
                error = 'მომხმარებელი უკვე არსებობს'
                conn.close()
                return render_template('auth_ge.html', auth_type='register', error=error)

            hashed_password = generate_password_hash(password, method='sha256')

            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
            conn.commit()
            conn.close()

            success = 'ანგარიში წარმატებით დარეგისტრირდა'

            return render_template('auth_ge.html', auth_type='register', success=success)
        else:
            error = 'დაერეგისტრირებისას წარმოიშალოს კაპსლოკის შეცდომები'
            return render_template('auth_ge.html', auth_type='register', error=error)
    return render_template('auth_ge.html', auth_type='register')


def login_ge():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = create_connection()
        if conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()

            conn.close()

            if user and check_password_hash(user[2], password):
                session['username'] = username
                return redirect(url_for('generate_pass'))
            else:
                error = 'მომხმარებელის სახელი ან პაროლი არასწორია'
                return render_template('auth_ge.html', auth_type='login', error=error)
        else:
            error = 'დაერეგისტრირებისას წარმოიშალოს კაპსლოკის შეცდომები'
            return render_template('auth_ge.html', auth_type='login', error=error)
    return render_template('auth_ge.html', auth_type='login')
