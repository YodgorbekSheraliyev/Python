from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField("Cafe Location", validators=[DataRequired()])
    open_time = StringField("Opening time", validators=[DataRequired()])
    close_time = StringField("Closing time", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", validators=[DataRequired()], choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️', '✘'])
    wifi_rating = SelectField(label="Wifi Rating", validators=[DataRequired()], choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪', '✘'])
    power_rating = SelectField(label="Power Outlet Rating", validators=[DataRequired()], choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌', '✘'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


# @app.route('/add')
# def add_cafe():
#     form = CafeForm()
#     if form.validate_on_submit():
#         print("True")
#     # Exercise:
#     # Make the form write a new row into cafe-data.csv
#     # with   if form.validate_on_submit()
#     return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location_url = form.location_url.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data

        with open('./cafe-data.csv', 'a+', encoding='utf-8') as file:
            file.write(f"\n{cafe},{location_url},{open_time},{close_time},{coffee_rating},{wifi_rating},{power_rating}")
            print(f"{cafe},{location_url},{open_time},{close_time},{coffee_rating},{wifi_rating},{power_rating}")
        return redirect('/cafes')
    return render_template('add.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)
