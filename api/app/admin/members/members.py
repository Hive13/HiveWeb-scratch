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

# TODO: how to return json object with sqlalchemy/flask
#* see: https://codeandlife.com/2014/12/07/sqlalchemy-results-to-json-the-easy-way/
# member profile
@app.route('/api/admin/members/profile', methods=["GET"])
def members():
    req_data = request.get_json()

    member_id = req_data['member_id']
    # build query, execute on get request
    s = sqlalchemy.text("""SELECT *
                            FROM members
                            WHERE member_id = x:""")
    result = conn.execute(s, x=member_id)
    rows = [{"member": row['member_id'], "member name": row['lname']} for row in result]
    return jsonify(rows)