from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import DocForm
from .messages import data_validation_message, delete_document_error
from .models import Document, Version
from .utils import data_is_valid


@app.route('/')
def index():
    object_list = Document.select()
    return render_template('index.html', object_list=object_list)


@app.route('/create', methods=['GET', 'POST'])
def create_document():
    form = DocForm()
    if form.validate_on_submit():
        data = {
            'title': form.title.data,
            'content': form.content.data,
        }
        with db.atomic():
            new_doc, created = Document.get_or_create(**data)
            if created:
                Version.create(document=new_doc.id, serialized_data=data)
        return redirect(url_for('document_detail', id=new_doc.id))
    return render_template('create.html', form=form)


@app.route('/document/<int:id>/')
def document_detail(id):
    document = Document.get_by_id(id)
    versions = document.versions.order_by(Version.date.desc())
    versions = [version.to_dict() for version in versions]
    context = {
        'obj': document,
        'versions': versions,
    }
    return render_template('doc_detail.html', **context)


@app.route('/document/<int:id>/update', methods=['GET', 'POST'])
def document_update(id):
    document = Document.get_by_id(id)
    form = DocForm(obj=document)
    context = {
        'form': form,
        'is_edit': True,
    }
    if form.validate_on_submit():
        data = {
            'title': form.title.data,
            'content': form.content.data,
            'on_delete': form.on_delete.data,
        }
        if not data_is_valid(data, document):
            flash(data_validation_message)
            return render_template('create.html', **context)
        with db.atomic():
            Document.update(**data).where(Document.id == id).execute()
            Version.create(document=document.id, serialized_data=data)
        return redirect(url_for('document_detail', id=document.id))
    return render_template('create.html', **context)


@app.route('/document/<int:id>/delete/')
def document_delete(id):
    document = Document.get_by_id(id)
    if not document.on_delete:
        flash(delete_document_error)
        return redirect(url_for('document_detail', id=id))
    versions = document.versions.order_by(Version.date.desc())
    with db.atomic():
        document.delete().execute()
        for version in versions[1::]:
            version.delete().execute()
    return redirect(url_for('index'))
