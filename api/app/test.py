from app import app

@app.route("/api/test")
def test():
    return {'message': 'Sucess', 'data': 'This is how this works'}