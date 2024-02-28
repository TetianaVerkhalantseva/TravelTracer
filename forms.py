from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, InputRequired, EqualTo
from wtforms import ValidationError
from database import Database


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Please enter your email"), Email(message="Inputs must be in email format")])
    password = PasswordField("Password", validators=[DataRequired(message="Please enter your password")])
    submit = SubmitField("Log in")


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(5, 40), Email(message="Inputs must be in email format")])
    username = StringField("Username", validators=[DataRequired(), Length(3, 30, message="Minimun 3 characters")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="Minimum 8 characters")])
    password2 = PasswordField('Confirm password', validators=[DataRequired(), EqualTo("password", message="Passwords must match")])
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    submit = SubmitField('Register')

    #def validate_email(self, field):
    #    with Database() as db:
    #        email = field.data.lower()
    #        if db.queryOne("SELECT * FROM user Where email = %s ", (email,)):
    #            raise ValidationError("Email already registered")
    #
    #def validate_username(self, field):
    #    with Database() as db:
    #        username = field.data
    #        if db.queryOne("SELECT * FROM user Where username = %s ", (username,)):
    #            raise ValidationError("Username already registered")
