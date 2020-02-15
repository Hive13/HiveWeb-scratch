#!/usr/bin/env python3
#########################################################################
# Scratch code to connect to HiveWeb database
# Authors: Chris Hodapp
# 2020-01-18, Hive13 Cincinnati
#########################################################################

# Depends on: sqlalchemy, pg8000
# (other drivers may work too)

import sqlalchemy
import urllib.parse

from creds import db_password

import db

user = "access"
host = "honeycomb.at.hive13.org"
dbname = "door"
driver = "pg8000"

# format is: dialect+driver://username:password@host:port/database
url = "postgresql+{}://{}:{}@{}/{}".format(
    driver,
    user,
    urllib.parse.quote_plus(db_password),
    host,
    dbname,
)
print("Using URL: {}".format(url))
engine = sqlalchemy.create_engine(url, echo=True)

# Bind to engine & connect:
db.metadata.bind = engine
conn = engine.connect()

# Put together a query:
s = sqlalchemy.sql.\
    select([db.members]).\
    order_by(db.members.c.created_at.desc())
result = conn.execute(s)
for row in result:
    print("Member ID: {member_id}, name: {fname} {lname}, since: {created_at}".format(
        **row))
