from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer, Boolean, Enum

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///d63-2.db"


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
    return render_template('index.html', books=all_books)

@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title=request.form['title'],
                author=request.form['author'],
                rating=request.form['rating']
            )
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/books/<int:id>/delete')
def delete_book(id:int):
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalars().all()
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect('/')

@app.route('/books/<int:id>', methods=["GET", "POST"])
def edit_book(id):
    # book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    book = db.get_or_404(Book, id)
    if request.method == "POST":
        rating = request.form.get("rating")
        book.rating = rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)
if __name__ == "__main__":
    app.run(debug=True)