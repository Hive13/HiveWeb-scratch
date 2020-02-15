from app import app
import os
import markdown

@app.route("/")
def index():
    """Present readme as documentation on index route"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)
