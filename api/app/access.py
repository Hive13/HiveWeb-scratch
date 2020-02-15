import random
import json
import hashlib
import requests

from creds import DEVICE, DEVICE_KEY

postURL = "http://intweb.at.hive13.org/api/access"

# for access code
def get_random_response(size=16):
    return [random.randint(0, 255) for _ in range(size)]

def get_checksum(key, data):
    s = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    print(s)
    m = hashlib.sha512()
    m.update(key)
    m.update(s)
    return m.hexdigest().upper()

# door access
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