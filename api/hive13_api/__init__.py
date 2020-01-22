# markdown and os are for rendering README.md as HTML on index route
import markdown
import os

# import framework(s)
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# create flask instance
app = Flask(__name__)

# create api
api = Api(app)

@app.route("/")
def index():
    """Present readme as documentation on index route"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

class test(Resource):
    def get(self):
        some_variable = 'Hive13 Rocks!!'
        
        # test route to show how other routes can be implemented
        return {'message': 'Success', 'data': some_variable}

api.add_resource(test, '/test')