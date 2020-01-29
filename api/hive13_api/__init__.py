# markdown and os are for rendering README.md as HTML on index route
import markdown
import os
import urllib.parse
import sqlalchemy
import db

from creds import db_password


# import framework(s)
from flask import Flask, g, jsonify
from flask_restful import Resource, Api, reqparse

# create flask instance
app = Flask(__name__)

# create api
api = Api(app)

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

# Bind to engine & connect:
db.metadata.bind = engine
conn = engine.connect()

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
class Test(Resource):
    def get(self):
        some_variable = 'Hive13 Rocks!!'
        
        # test route to show how other routes can be implemented
        return {'message': 'Success', 'data': some_variable}

class Members(Resource):
    def get (self):
        # build query, execute on get request
        s = sqlalchemy.sql.\
            select([db.members]).\
            limit(10).\
            order_by(db.members.c.created_at.desc())
        result = conn.execute(s)
        rows = [{"member": row['member_id']} for row in result]
        return jsonify(rows)

api.add_resource(Test, '/test')
api.add_resource(Members, '/members')