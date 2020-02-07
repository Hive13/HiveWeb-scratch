# markdown and os are for rendering README.md as HTML on index route
import markdown
import os
import urllib.parse
import sqlalchemy
import json
import random
import hashlib
import requests

import db

from creds import db_password, DEVICE, DEVICE_KEY


# import framework(s)
from flask import Flask, g, jsonify

# create flask instance
app = Flask(__name__)

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

postURL = "http://intweb.at.hive13.org/api/access"

print("Using URL: {}".format(url))
engine = sqlalchemy.create_engine(url, echo=True)

# Bind to engine & connect (comment out for dev outisde of hive):
db.metadata.bind = engine
conn = engine.connect()

def get_random_response(size=16):
    return [random.randint(0, 255) for _ in range(size)]

def get_checksum(key, data):
    s = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    print(s)
    m = hashlib.sha512()
    m.update(key)
    m.update(s)
    return m.hexdigest().upper()

### ------- Begin Routing ------- ###

@app.route("/")
def index():
    """Present readme as documentation on index route"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

# /test route returns a json object with message success and some_variable
@app.route("/api/test", methods=["GET"])
def test():
    return {'message': 'Sucess', 'data': 'This is how this works'}

@app.route('/api/members', methods=["GET"])
def members():
    # build query, execute on get request
    s = sqlalchemy.sql.\
        select([db.members]).\
        order_by(db.members.c.created_at.asc())
    result = conn.execute(s)
    rows = [{"member": row['member_id'], "member name": row['lname']} for row in result]
    return jsonify(rows)

@app.route('/api/access/door', methods=["POST"])
def member_door_access():
    msg = {
        "data": {
            "operation": "get_nonce",
            "version": 2,
            "random_response": get_random_response(),
        },
        "device": DEVICE,
    }

    cs = get_checksum(DEVICE_KEY, msg["data"])
    msg["checksum"] = cs

    print("Posting: {}".format(msg))
    res = requests.post(postURL, json = msg)
    print(res)
    print(res.json())
    return res.json()

@app.route('/api/access/vend/<incoming_badge_number>', methods=["GET"])
def vend(incoming_badge_number):
    s = sqlalchemy.text("""SELECT b.badge_number, m.vend_credits
                            FROM badge AS b
                            INNER JOIN members AS m ON m.member_id = b.member_id
                            WHERE b.badge_number = :x""")
    result = conn.execute(s, x=incoming_badge_number)
    rows = [{"vend_credits": row['vend_credits']} for row in result]
    return jsonify(rows)  

@app.route('/api/access/tool/', methods=["GET"])
def tool_access():
    pass