from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length 

class RegistrationForm(FlaskForm) :
  name = StringField("Full Name",validators=[DataRequired(message="we need your Name,it can't be empty")]) 
  email = StringField("Email",validators=[DataRequired(message="Email field is Required"),Email(message="Doesn't look like email")])
  password = PasswordField("Password",validators=[DataRequired(message="Password is Required"),Length(min=6,)])
  submit = SubmitField("Register")
