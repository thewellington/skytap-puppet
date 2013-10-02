#!/usr/bin/env python
#
#


import json
import urllib
import urllib2
from pprint import pprint

# Step 1, get gateway address

# Step 2, get metadata from gateway
url = "http://192.168.1.254/skytap"
#req = urllib2.Request(url)
with urllib2.urlopen(url) as response:
  new_metadata = getJson(response)
  print NEW DATA
  pprint (new_metadata)

# Step 3, get stored metadata
with open('samplejson.txt') as infile:
  old_metadata = json.load(infile)
  #pprint (data)
  pprint (old_metadata["id"])
  pprint (old_metadata["interfaces"][0]['ip'])

# Step 4, compare new and old metadata





# json Load
def getJson(input):
  data = json.load(input)
  return data