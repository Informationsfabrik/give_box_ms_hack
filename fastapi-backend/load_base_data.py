import requests
import json
import os

try:
    if os.environ['ENV'] == 'prod':
        server = 'https://api.givebox-ms.de/'
    else:
        server = 'http://localhost:8081/'
except:
    server = 'http://localhost:8081/'



def load_base_data(router,server = server):
    with open("data/"+router+".json") as json_file:
        data = json.load(json_file)
        for item in data:
            requests.post(server+router, json=item)

load_base_data("giveboxes")

load_base_data("users")


def load_demo_maintainer(router,server = server):
    with open("data/"+router+".json") as json_file:
        data = json.load(json_file)
        for item in data:
            requests.post(server+router+'/'+str(item['box_id'])+'/'+str(item['user_id']))

load_demo_maintainer("add_maintainer")