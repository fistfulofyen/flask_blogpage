from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=2,max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), Length(min=2,max=20), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # create a custom valudation incase same email used for regist
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() # or self.username should work too
        #if name is unique, then user is false
        if user:
            raise ValidationError('Username is taken, pick a new one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        #if name is unique, then user is false
        if user:
            raise ValidationError('Email is taken, pick a new one.')

class LoginForm(FlaskForm):
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=2,max=20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    # create a custom valudation incase same email used for regist
    def validate_username(self, username):
        if username.data != current_user.username:

            user = User.query.filter_by(username=username.data).first() # or self.username should work too
            #if name is unique, then user is false
            if user:
                raise ValidationError('Username is taken, pick a new one.')
    
    def validate_email(self, email):
        if email.data != current_user.email:

            user = User.query.filter_by(email=email.data).first()
            #if name is unique, then user is false
            if user:
                raise ValidationError('Email is taken, pick a new one.')
            
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        #if name is unique, then user is false
        if user is None:
            raise ValidationError('No account with that email')
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')