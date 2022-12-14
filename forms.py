from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCreateAccount(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
  password_confirmation = PasswordField('Password confirmation', validators=[DataRequired(), EqualTo('password')])
  btn_submit_create_account = SubmitField('Create account')


class FormLogin(FlaskForm):
  emaill = StringField('E-mail', validators=[DataRequired(), Email()])
  passwordl = PasswordField('Password', validators=[DataRequired(), Length(6,20)])
  remember_me = BooleanField('Remmember access data')
  btn_submit_login = SubmitField('Login')

