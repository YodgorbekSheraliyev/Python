from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice

"""
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.get("/random")
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = choice(cafes)
    cafe_dict = random_cafe.to_dict()
    response = {
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
        "has_sockets": random_cafe.has_sockets,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
    }
    return jsonify(cafe_dict)


@app.get("/all")
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes)


# HTTP POST - Create Record
@app.post("/add")
def add_cafe():
    name = request.form["name"]
    map_url = request.form["map_url"]
    img_url = request.form["img_url"]
    location = request.form["location"]
    seats = request.form["seat"]
    has_wifi = bool(request.form["has_wifi"])
    has_sockets = bool(request.form["has_sockets"])
    can_take_calls = bool(request.form["can_take_calls"])
    coffee_price = request.form["coffee_price"]
    if not (
        name
        and map_url
        and img_url
        and location
        and seats
        and has_wifi
        and has_sockets
        and can_take_calls
        and coffee_price
    ):
        return redirect("/")
    cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        seats=seats,
        has_wifi=has_wifi,
        has_sockets=has_sockets,
        can_take_calls=can_take_calls,
        coffee_price=coffee_price,
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.patch('update-price/<int:cafe_id>')
def update_cafe(cafe_id):
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    price = request.form.get("coffe_price")
    if not price:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    cafe_to_update.coffee_price = price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."})


# HTTP DELETE - Delete Record
@app.delete('/report-closed/<int:cafe_id>')
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if not api_key:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    if not cafe_to_delete:
        return jsonify({"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}), 404
    
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe from the database."})


if __name__ == "__main__":
    app.run(debug=True)
