import json
import time


with open('.\config.json', "r") as config:
    data = json.load(config)

print(data["username"])


