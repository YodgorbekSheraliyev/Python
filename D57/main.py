from flask import  Flask, render_template, url_for
import requests



app = Flask(__name__)

url = "https://api.npoint.io/643ade877c3d59ee151a"
data  = requests.get(url).json()
@app.route('/')
def index():
    return render_template('index.html', title='Home', data=data)
# @app.route('/api')

@app.route('/blog')
def go_blog():
    global url
    response = requests.get(url)
    all_posts = response.json()
    return render_template('index.html', data=all_posts)
    pass



app.run(debug=True)
