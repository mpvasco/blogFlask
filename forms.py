from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCreateAccount(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
  password_confirmation = PasswordField('Password confirmation', validators=[DataRequired(), EqualTo('password')])
  btn_submit_create_account = SubmitField('Create account')


class FormLogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired(), Length(6,20)])
  btn_submit_login = SubmitField('Login')

