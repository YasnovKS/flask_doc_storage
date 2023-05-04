import json
from datetime import datetime as dt

from peewee import *

from . import db


class BaseModel(Model):
    class Meta:
        database = db


class Document(BaseModel):
    title = CharField(max_length=100)
    content = TextField()
    date = DateTimeField(default=dt.now())
    on_delete = BooleanField(default=False)


class Version(BaseModel):
    document = ForeignKeyField(model=Document, backref='versions')
    serialized_data = TextField()
    date = DateTimeField(default=dt.now)

    def to_dict(self):
        return json.loads(self.serialized_data)

    def serialize(self, data: dict):
        return json.dumps(data, ensure_ascii=False)

    def save(self, *args, **kwargs):
        self.serialized_data = self.serialize(self.serialized_data)
        return super().save(*args, **kwargs)
