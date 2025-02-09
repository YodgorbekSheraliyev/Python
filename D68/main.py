from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin,AnonymousUserMixin, login_user, LoginManager, login_required, current_user, logout_user
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.secret_key = "abc"

login_manager= LoginManager()
login_manager.init_app(app)



# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, AnonymousUserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.context_processor
def set_globabl_vars():
    return {
        "logged_in": session.get("is_auth"),
    }

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        if not (name and email and password):
            flash("All fields are required", "error")
            return redirect(url_for("register"))
        exist_user = db.session.get(User, email)
        if exist_user:
            flash("This user already registered", "error")
            return redirect('/login')
        
        new_user = User(
            name = name,
            email = email,
            password = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)
        )
        db.session.add(new_user)
        db.session.commit()
        session['is_auth'] = True
        return render_template("secrets.html", name=name)
    return render_template("register.html")


@app.route('/login')
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if not (email and password):
            flash("All fields are required", "error")
            return redirect(url_for("login"))
        
        exist_user = db.session.get(User, email)
        is_password_match = check_password_hash(exist_user.password, password)
        if is_password_match:
            login_user(exist_user)
            session['is_auth'] = True

            return redirect('/')
            
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory=path.abspath(path.join(path.dirname(__file__), "static", 'files')),
        path='cheat_sheet.pdf',
         as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
