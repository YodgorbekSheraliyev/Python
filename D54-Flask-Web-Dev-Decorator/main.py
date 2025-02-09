from flask import Flask
from markupsafe import escape
# import index, requests

app = Flask(__name__)


@app.route('/<name>/<user_id>')
def hello_world(name, user_id):
    return f"{name, user_id}"


@app.route('/api')
def get_api_route():
    return f"<h1>qwdqwdfqe</h1>"

app.run(debug=True)