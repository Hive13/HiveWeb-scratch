from app import app
from flask import jsonify
from flask import request
import sqlalchemy
import db
import urllib
import json
import hashlib

# get_checksum function shamelessly stolen from Hodapp's reference implementation
def get_checksum(key, data):
    s = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    print(s)
    m = hashlib.sha512()
    m.update(key)
    m.update(s)
    return m.hexdigest().upper()

# primary door access endpoint
@app.route('/api/access', methods=["POST"])
def access_protocol():
    req_payload = request.get_json()
    #device name
    device = req_payload['device']

    # uppercase SHA512 hash of the data json object with the device key from the database prepended
    # serialized in resursive alphabetical order and all whitespace removed
    checksum = req_payload['checksum']

    # All the important stuff is in here.
    req_data = req_payload['data']

    # debug: show the data object in whatever format get_checksum needs
    jsontest = json.dumps(req_data, sort_keys=True, separators=(",", ":")).encode()
    return jsontest

    # Recompute the checksum to do some comparisons.
    #computed_checksum = get_checksum(device_key, req_data)