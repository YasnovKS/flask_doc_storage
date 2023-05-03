from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class DocForm(FlaskForm):
    title = StringField(
        'Наименование документа',
        validators=[
            DataRequired(
                message='Обязательно для заполнения'),
            Length(1, 100)
        ]
    )
    content = TextAreaField(
        'Содержание документа',
        validators=[
            DataRequired(
                message='Обязательно для заполнения'),
        ]
    )
    submit = SubmitField('Создать')
