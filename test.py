#!/usr/bin/env python
#
#

# import modules
import json
import urllib
import urllib2
import hashlib
from pprint import pprint

# set variables
url = "http://192.168.1.254/skytap"
json_path = 'samplejson.txt'

# build functions
def getJSON(data):
  result = json.load(data)
  return result

def get_current_metadata():
  response = urllib2.urlopen(url)
  current_metadata = getJSON(response)
  result = current_metadata["id"]
  print result

def get_stored_metadata():
  with open(json_path) as infile:
    stored_metadata = getJSON(infile)
    result = stored_metadata["id"]
    print result


###############################################################################    
# Main Function
def main ():

# if the file at json_path exists:

  current_metadata = get_current_metadata()
  current_id = 

# compare the values
  if (current_id == stored_id):
    print ('OK!')
  else:
    print ('Something is wrong!')

# Call main()
if __name__ == '__main__':
  main()