import requests
import json

def post_data(payload):
    id = str(payload["id"])
    res = requests.post("http://129.173.143.240:8000/api/pods/" + id + "/", json=payload)
    print(res.status_code)

map = {}
map["R1"] = 1
map["R2"] = 2
map["R3"] = 3
map["R4"] = 4
map["S1"] = 5
map["S2"] = 6
map["S3"] = 7
map["AP1"] = 8
map["AP2"] = 9
map["TS"] = 10

def mapper(obj):
    name = obj["name"]
    if obj["type"] == "router" or obj["type"] == "switch" or obj["type"] == "ts":
        return map[name[-2:]]
    elif obj["type"] == "accessPoint":
        return map[name[-3:]]


with open('json_file') as f:
    data = json.load(f)
    for i in data:
        id = int(i.split(" ")[1])
        if id <= 5:
            continue

        payload = {}
        devices = []
        payload["id"] = int(id)
        payload["devices"] = devices

        data_devices = data[i]
        for device in data_devices:
            dev = {}
            dev["device"] = {}
            dev["device"]["id"] = int(mapper(device))
            dev["dev_url"] = device["url"]
            devices.append(dev)
        print(payload)
        post_data(payload)
