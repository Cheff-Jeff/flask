from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, IPAddress, Length, EqualTo

class LoginForm(FlaskForm):
  username = StringField('Username', 
    validators=[DataRequired()], 
    render_kw={"placeholder": "User name"})
  password = StringField('Password', 
    validators=[DataRequired()], 
    render_kw={"placeholder": "Password", "type": "password"})
  submit = SubmitField('Login')

class RegisterForm(FlaskForm):
  username = StringField('Username', 
    validators=[DataRequired(), Length(min=2, max=20)], 
    render_kw={"placeholder": "User name"})
  password = StringField('Password', 
    validators=[DataRequired()], 
    render_kw={"placeholder": "Password", "type": "password"})
  confirmpassword = StringField('Confirm Password', 
    validators=[DataRequired(), EqualTo('password')], 
    render_kw={"placeholder": "Confirm Password", "type": "password"})
  submit = SubmitField('Register')

class IPform(FlaskForm):
  IPaddress = StringField('IPaddress', 
    validators=[DataRequired(), IPAddress(ipv4=True, ipv6=False, message="This is no ip")],
    render_kw={"placeholder": "Your ip addres"})
  submit = SubmitField('Add ip')