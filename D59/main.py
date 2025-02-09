from flask import Flask, render_template
import requests

url = "https://api.npoint.io/674f5423f73deab1e9a7"

app = Flask(__name__)

@app.route('/')
def home():
    posts= requests.get(url).json()
    return render_template("index.html", posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id: int):
    posts= requests.get(url).json()
    post = next(p for p in posts if p["id"] == id)
    return render_template('post.html', post=post)



if __name__ == "__main__":
    app.run(debug=True)