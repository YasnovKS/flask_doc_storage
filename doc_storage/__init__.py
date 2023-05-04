import os

from dotenv import load_dotenv
from flask import Flask
from peewee import SqliteDatabase

load_dotenv()

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db_name = os.getenv('DATABASE')
db = SqliteDatabase(db_name)
