#!/usr/bin/env python
#
#

# import modules
import json
import urllib
import urllib2
import hashlib
from pprint import pprint

def getJSON(data):
   result = json.load(data)
   return result


# Main Function
def main ():

# get current metadata from skytap
  url = "http://192.168.1.254/skytap"
  response = urllib2.urlopen(url)
  new_metadata = getJSON(response)
  pprint (new_metadata)

# get stored metadata fron disk
  with open('samplejson.txt') as infile:
    old_metadata = getJSON(infile)
    #data = json.load(infile)
    #pprint (data)
    pprint (old_metadata["id"])
    pprint (old_metadata["interfaces"][0]['ip'])

# Call main()
if __name__ == '__main__':
  main()