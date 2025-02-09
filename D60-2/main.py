from flask import Flask, render_template, request
import requests, smtplib
user = ""
password = ""

def send_mail(sender, receiver, text):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.starttls()
        smtp.login(user=user, password=password)
        smtp.sendmail(from_addr=sender, to_addrs=receiver, msg=f"Subject:  This is test email \n\n {text} ")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact', methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_mail(user, email, message)
        return f"<h1>Successfully sent the message</h1>"
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True, port=5001)
