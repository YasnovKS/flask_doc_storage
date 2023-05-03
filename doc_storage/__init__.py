import os

from peewee import SqliteDatabase
from flask import Flask

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates')

db_name = os.getenv('DATABASE')
db = SqliteDatabase(db_name)
