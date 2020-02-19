from flask import Flask, g, jsonify, request
import json
import random
import hashlib
import requests

app = Flask(__name__)

# Import global config
from app import config

# Import credentials module
from app import creds

# Initialize database
import sqlalchemy
import db

db_url = "postgresql+{}://{}:{}@{}/{}".format(
    config.db_driver,
    config.db_user,
    urllib.parse.quote_plus(creds.db_password),
    config.db_host,
    config.db_name,
)

db_engine = sqlalchemy.create_engine(db_url, echo=True)

db.metadata.bind = db_engine
db_conn = db_engine.connect()

# import endpoint packages
from app import test
from app import tool
from app import index
from app.admin.members import members
from app import vend