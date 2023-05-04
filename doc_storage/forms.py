from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, TextAreaField
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
    on_delete = BooleanField('Пометить на удаление')
    submit = SubmitField('Создать')
