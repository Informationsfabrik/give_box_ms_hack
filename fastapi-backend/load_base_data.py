import requests
import json


def load_base_date(router):
    with open("data/"+router+".json") as json_file:
        data = json.load(json_file)
        for item in data:
            requests.post('http://127.0.0.1:8081/'+router, json=item)

load_base_date("giveboxes")

load_base_date("users")