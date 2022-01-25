from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
import wtforms.validators


class RegistrationForm(FlaskForm):
    username = \
        StringField(
            'Username', validators=[wtforms.validators.DataRequired(), wtforms.validators.Length(min=2, max=20)])
    email = StringField('Email', validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    password = PasswordField('Password', validators=[wtforms.validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[wtforms.validators.DataRequired(),
                                                                     wtforms.validators.EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    password = PasswordField('Password', validators=[wtforms.validators.DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
