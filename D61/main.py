from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

# class MyForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired()])
#     password = StringField('Paddword', validators=[DataRequired()])



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# class LoginForm(FlaskForm):
#     email = StringField(label="Email", validators=[DataRequired(), Email()])
#     password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
#     login = SubmitField(label="Log in")

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "dwdwef"


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email =="admin@email.com" and password == "12345678":
            return render_template('success.html')
        else: 
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
