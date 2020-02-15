from app import app

@app.route('/api/access/tool/', methods=["GET"])
def tool_access():
    return {"message": "hello world"}