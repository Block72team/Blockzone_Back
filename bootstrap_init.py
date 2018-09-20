# coding=utf-8
'Init the app'
__author__ = 'Jiateng Liang'
from flask import Flask, Blueprint
from config.config import *
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

# Environment setting
if len(sys.argv) <= 1 or sys.argv[1] == 'dev':
    app.config.from_object(Config)
elif sys.argv[1] == 'test':
    app.config.from_object(TestConfig)
elif sys.argv[1] == 'prod':
    app.config.from_object(ProdConfig)

# Database init
db = SQLAlchemy(app)


