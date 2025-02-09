from flask import Flask, render_template
import requests
import post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

post = post.Post(blog_url)


app = Flask(__name__)

@app.route('/')
def home():
    my_posts = requests.get(blog_url).json()
    return render_template("index.html", posts=my_posts)

@app.route("/blog/<int:id>")
def blog(id: int):
    single_post = post.get_by_id(id)
    return render_template('post.html', post=single_post)
    



if __name__ == "__main__":
    app.run(debug=True)
