from app import app
import sqlalchemy
import urllib.parse
from flask import jsonify
import db

from creds import db_password, DEVICE, DEVICE_KEY

user = "access"
host = "honeycomb.at.hive13.org"
dbname = "door"
driver = "pg8000"

# designate url
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

# Bind to engine & connect (comment out for dev outisde of hive):
db.metadata.bind = engine
conn = engine.connect()

@app.route('/api/members', methods=["GET"])
def members():
    # build query, execute on get request
    s = sqlalchemy.sql.\
        select([db.members]).\
        order_by(db.members.c.created_at.asc())
    result = conn.execute(s)
    rows = [{"member": row['member_id'], "member name": row['lname']} for row in result]
    return jsonify(rows)