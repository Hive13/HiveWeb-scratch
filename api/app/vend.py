from app import app
from flask import jsonify
import sqlalchemy
import urllib
import db

from app.creds import db_password

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


@app.route('/api/access/vend/<incoming_badge_number>', methods=["GET"])
def vend(incoming_badge_number):
    s = sqlalchemy.text("""SELECT b.badge_number, m.vend_credits
                            FROM badge AS b
                            INNER JOIN members AS m ON m.member_id = b.member_id
                            WHERE b.badge_number = :x""")
    result = conn.execute(s, x=incoming_badge_number)
    rows = [{"vend_credits": row['vend_credits']} for row in result]
    return jsonify(rows)  