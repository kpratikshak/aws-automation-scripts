import json
import requests
from socket import timeout
import logging

def hit_endpoint(url):
    list =[]
    if (url!=""):
        data = requests.get(url)
        dump = data.json()
        print(dump['count'])
        
        for link in dump["entries"]:
            print(link['Link'])
            try:
                data2 = requests.get(link['Link'])
                dump2 = data2.json()
                list.append(dump2)