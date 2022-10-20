from flask import Flask, url_for, request, redirect
from flask.templating import render_template
from database import get_database
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        db = get_database()
        user_cursor = db.execute('SELECT * FROM users WHERE name = ?', [name])
        user = user_cursor.fetchone()

        if user:
            if check_password_hash(user['password'], password):
                return redirect(url_for('dashboard'))
            else:
                error = " user/password did not match"
    return render_template('login.html', loginerror = error)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        
        db = get_database()
        db.execute('INSERT INTO users (name, password) VALUES (?, ?)', [name, hashed_password])
        db.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/addnewemployee')
def addnewemployee():
    return render_template('addnewemployee.html')

@app.route('/singleemployee')
def singleemployee():
    return render_template('singleemployee.html')

@app.route('/updateemployee')
def updateemployee():
    return render_template('updateemployee.html')


def logout():
    render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)