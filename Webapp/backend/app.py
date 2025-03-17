from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
import mysql.connector
import os

app = Flask(__name__, template_folder="/app/templates")

app.secret_key = 'f4c8a14c60794f4a8e7688e2a7587b10'  # Required for session management

# Connect to MySQL database
db = mysql.connector.connect(
    host="database",  
    user="testuser",
    password="TestPassword12!",
    database="testdb"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        session['message'] = "User Registered Successfully!"  # Store success message
    except mysql.connector.IntegrityError:
        session['message'] = "Email already registered!"

    return redirect(url_for('home'))  # Redirect to homepage

@app.route('/history')
def history():
    cursor.execute("SELECT name, email FROM users")
    users = cursor.fetchall()  # Fetch all user data
    return render_template('history.html', users=users)  

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    