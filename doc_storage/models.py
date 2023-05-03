from peewee import *
from . import db
import json
from datetime import datetime as dt


class Document(Model):
    title = CharField(max_length=100)
    content = TextField()
    date = DateTimeField(default=dt.now())

    class Meta:
        database = db


class Version(Model):
    document = ForeignKeyField(model=Document)
    serialized_data = TextField()
    message = CharField()
    date = DateTimeField(default=dt.now)

    def __init__(self, data: dict) -> None:
        self.serialized_data = self.serialize(data)
        return super().__init__()

    def to_dict(self):
        return json.loads(self.serialized_data)

    def serialize(self, data: dict):
        return json.dumps(data)
