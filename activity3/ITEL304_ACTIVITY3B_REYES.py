from re import T
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    age = request.args.get('age', 'World')
    favfood = request.args['favfood']
    if favfood == '':
        msg = "You didn't tell me you favorite food."
    else:
        msg = "I'm " + age + " and I like " + favfood + ', too.'

    return """
        <html><body>
            <h2>Hello, {0}!</h2>
            {1}
        </body></html>
        """.format(username, msg)

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
