from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String

app = Flask(__name__)

# Create Base Clasee
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

# Create the extension
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', review={self.review})>"


with app.app_context():
    db.create_all()


# with app.app_context():
#     new_book = Book(title="Harry Potterr", author= "J. K. Rowling", review= 9.3)
#     new_book2 = Book(title="Harry Potterrewfq34frq34g3", author= "J.eragrwgfr K. Rowling", review= 9.3)
#     db.session.add(new_book)
#     db.session.add(new_book2)
#     db.session.commit()
#     print("Created")

with app.app_context():
    book_to_update = db.session.execute(db.select(Book)).scalars()
    if book_to_update:
        book_to_update.title = "Mwefwefew"
        db.session.commit()

with app.app_context():
    bookt_to_delete = db.session.execute(db.select(Book).where(Book.id==2)).scalar_one_or_none()
    print(bookt_to_delete)
    if bookt_to_delete:
        db.session.delete(bookt_to_delete)
        db.session.commit()

with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.review == 9.3))
    all_books = result.scalars()
    print(all_books.fetchall())



# @app.route("/")
# def home():
#     return render_template("index.html", books=all_books)


# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "GET":
#         return render_template("add.html")
#     all_books.append(request.form.to_dict())
#     return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
