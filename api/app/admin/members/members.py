from app import app
import sqlalchemy
import urllib.parse
from flask import jsonify, request
import db

from creds import db_password, DEVICE, DEVICE_KEY

#? is there a way for use to move this out of this file?
# I think a lot of files will be using this data along with the `url` var and db connection. 
# can we do this in __init__.py?
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

# create sqlalchemy engine
# ? Should echo be True here?
engine = sqlalchemy.create_engine(url, echo=True)

# Bind to engine & connect (comment out for dev outisde of hive):
db.metadata.bind = engine
conn = engine.connect()

# member profile
@app.route('/api/admin/members/profile/', methods=['GET', 'POST'])
def members():
    req_data = request.get_json()

    member_id = req_data['member_id']
    # build query, execute on get request
    s = sqlalchemy.text("""SELECT *
                            FROM members
                            WHERE member_id = :x
                        """)
    
    # try to execute the query, except when it returns an error.
    try:
        result = conn.execute(s, x=str(member_id))
        rows = [dict(row) for row in result]
        return jsonify(rows)
    except:
        error_message = [{"result": 0, "message": "Invalid Member ID"}]
        return jsonify(error_message)
