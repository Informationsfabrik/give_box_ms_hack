import requests
import json


def load_base_data(router):
    with open("data/"+router+".json") as json_file:
        data = json.load(json_file)
        for item in data:
            requests.post('http://127.0.0.1:8081/'+router, json=item)

#load_base_data("giveboxes")

#load_base_data("users")


def load_demo_maintainer(router):
    with open("data/"+router+".json") as json_file:
        data = json.load(json_file)
        for item in data:
            requests.post('http://127.0.0.1:8081/'+router+'/'+str(item['box_id'])+'/'+str(item['user_id']))

load_demo_maintainer("add_maintainer")