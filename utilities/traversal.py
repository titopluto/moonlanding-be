import json

map = {}
with open('json_file') as f:
    data = json.load(f)
    for i in data:
        devices = data[i]
        for dev in devices:
            if dev["type"] not in map:
                map[dev["type"]] = []

            map[dev["type"]].append(dev["model"])
            map[dev["type"]] = sorted(map[dev["type"]])

print(map)