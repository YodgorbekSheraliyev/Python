from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

movies_api = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOWU4OGRlODMyNzYwNjRlMTJmZjlmZjIwMjg1MTc5NyIsIm5iZiI6MTY4MDI4NjU1Ny42OTIsInN1YiI6IjY0MjcyMzVkYTNlNGJhMDExMTQ5OWU5YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.R8QDY50W7dnMNwtrXlZhjtMqDr-7VoIxOOCrkIqHx14",
}
movies = []


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///d64.db"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String)
    img_url: Mapped[str] = mapped_column(String)


class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g 7.5")
    review = StringField("Your review", validators=[DataRequired()])
    done = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField(
        "Movie Title", validators=[DataRequired("Please insert name of the movie")]
    )
    button = SubmitField("Add Movie")


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars().all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["POST", "GET"])
def edit_rating():
    id = request.args.get("id")
    movie_form = EditForm()

    if request.method == "POST":
        movie = db.session.get(Movie, id)
        if not movie:
            return redirect('/')
        rating = request.form["rating"]
        review = request.form["review"]
        if rating :
            movie.rating = rating
        if review:
            movie.review = review
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=movie_form)
        


@app.route("/movies/delete")
def delete_movie():
    id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect("/")


@app.route("/find", methods=["GET", "POST"])
def find_movie():

    if request.method == "GET":
        form = AddMovieForm()
        return render_template("add.html", form=form)

    if request.method == "POST":
        title = request.form["title"]
        return redirect(url_for("select_movie", title=title))


@app.route("/select/movie", methods=["GET", "POST"])
def select_movie():
    global movies
    title = request.args.get("title")
    movies = requests.get(movies_api, headers=headers, params={"query": title}).json()
    print(movies)
    return render_template("select.html", movies=movies['results'])


@app.route("/add-to-db")
def add_movie():
    id = int(request.args.get("movie_id"))
    url = f"https://api.themoviedb.org/3/movie/{id}"
    movie = requests.get(url, headers=headers).json()
    print(movie)
    if not movie:
        return "Movie not found", 404
    new_movie = Movie(
        title=movie["title"],
        year=movie["release_date"],
        description=movie["overview"],
        rating=0.0,
        ranking=0,
        review="",
        img_url=f"https://image.tmdb.org/t/p/original/{movie['backdrop_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit_rating', id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
