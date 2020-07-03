#!/usr/bin/env python3
#########################################################################
# Scratch code to authenticate with intweb device access
# Authors: Chris Hodapp
# 2020-01-19, Hive13 Cincinnati
#########################################################################

# See:
# https://wiki.hive13.org/view/Access_Protocol
# https://github.com/Hive13/hive-rfid-door-controller

# This is planned, tentatively, to only be vestigial.

import json
import random
import hashlib

import requests

# DEVICE is string, DEVICE_KEY is bytestring
from creds import DEVICE, DEVICE_KEY

URL = "https://intweb.at.hive13.org/api/access"

def get_random_response(size=16):
    return [random.randint(0, 255) for _ in range(size)]

def get_checksum(key, data):
    s = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    print(s)
    m = hashlib.sha512()
    m.update(key)
    m.update(s)
    return m.hexdigest().upper()

def main():
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
    res = requests.post(URL, json = msg)
    print(res)
    if res.status_code != requests.codes.ok:
        raise Exception("Received HTTP error")
    print("Status code OK")
    print(res.json())
    d = res.json()
    err = d["data"].get("error", None)
    if err is not None:
        raise Exception("Server reported error: {}".format(err))
    nonce = d["data"]["new_nonce"]
    print("New nonce: {}".format(nonce))
    msg2 = {
        "data": {
            "operation": "access",
            "version": 2,
            "random_response": get_random_response(),
            "nonce": nonce,
            "item": "main_door",
        },
        "device": DEVICE,
    }
    cs = get_checksum(DEVICE_KEY, msg2["data"])
    msg2["checksum"] = cs
    print("Posting: {}".format(msg2))
    res = requests.post(URL, json = msg2)
    print(res)
    if res.status_code != requests.codes.ok:
        raise Exception("Received HTTP error")
    print(res.json())
    d = res.json()
    if not d["data"]["nonce_valid"]:
        raise Exception("Server reported invalid nonce")
    err = d["data"].get("error", None)
    if err is not None:
        raise Exception("Server reported error: {}".format(err))

if __name__ == "__main__":
    main()
