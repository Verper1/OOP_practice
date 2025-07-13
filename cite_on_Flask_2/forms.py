from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
    nickname = StringField("Никнейм: ", validators=[DataRequired()])
    password = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Подтвердить")
