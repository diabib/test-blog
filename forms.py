from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class Register(FlaskForm):
    username = StringField(label='UserName',validators=[DataRequired(), Length(min=2, max=5)])
    email = StringField(label='Email', validators=[DataRequired(),Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Submit')


class Login(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    remember = BooleanField(label='Remember me')
    submit=SubmitField(label='login')