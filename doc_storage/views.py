from flask import render_template

from . import app
from .models import Document
from .forms import DocForm


@app.route('/')
def index():
    object_list = Document.select()
    return render_template('index.html', object_list=object_list)


@app.route('/create', methods=['GET', 'POST'])
def create_document():
    form = DocForm()
    return render_template('create.html', form=form)
