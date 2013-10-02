#!/usr/bin/env python
#
#


import json

from pprint import pprint
json_data=open('samplejson.txt')

data = json.load(json_data)
#pprint (data)
pprint (data["id"])
pprint (data["interfaces"][0]['ip'])

json_data.close()