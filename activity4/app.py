from re import template
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def base():
    return render_template("base.html")

app.run(host="localhost", debug=True)