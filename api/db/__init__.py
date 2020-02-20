# Import global config
from db import config

# Import credentials module
from app import creds

# Initialize database
import sqlalchemy
from db import db
import urllib

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