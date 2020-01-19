#########################################################################
# Scratch code to connect to HiveWeb database
# Authors: Chris Hodapp
# 2020-01-18, Hive13 Cincinnati
#########################################################################

# Depends on: sqlalchemy, pg8000
# (other drivers may work too)

import sqlalchemy
import urllib.parse

from creds import password

# dialect+driver://username:password@host:port/database
user = "access"
host = "honeycomb.at.hive13.org"
db = "door"
driver = "pg8000"
url = "postgresql+{}://{}:{}@{}/{}".format(
    driver,
    user,
    urllib.parse.quote_plus(password),
    host,
    db,
)
print("Using URL: {}".format(url))
engine = sqlalchemy.create_engine(url, echo=True)

