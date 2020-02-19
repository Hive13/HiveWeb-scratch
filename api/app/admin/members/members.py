from app import app
import sqlalchemy
import urllib.parse
from flask import jsonify, request

from app import db_conn

# member profile
@app.route('/api/admin/members/profile', methods=['GET', 'POST'])
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
        result = db_conn.execute(s, x=str(member_id))
        rows = [dict(row) for row in result]
        return jsonify(rows)
    except:
        error_message = [{"result": 0, "message": "Invalid Member ID"}]
        return jsonify(error_message)
