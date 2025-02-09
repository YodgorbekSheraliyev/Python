from flask import Flask, render_template
from os import path
app = Flask(__name__, template_folder=path.join(path.dirname(__file__), 'templates'))

@app.route('/')
def get_home():
    return render_template('index.html')

app.run(debug=True)