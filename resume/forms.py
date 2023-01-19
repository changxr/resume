from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp
from resume.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired(),Regexp('^[a-z]{6,8}$',message='Your username should be between 6 and 8 characters long, and can only contain lowercase letters.')])
  password = PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_pass', message='password do not match. Try again')])
  confirm_pass = PasswordField('Confirm Password',validators=[DataRequired()])
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Username already exist. Please choose a different one.')



class LoginForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')


class PostForm(FlaskForm):
  title = StringField('Title',  validators=[DataRequired()])
  content = TextAreaField('Content',validators=[DataRequired()])
  on= SelectField("On", choices=[('learning', 'learning'), ('work', 'work'), ('school', 'school'),("future", 'future')])
  submit = SubmitField('Post')


