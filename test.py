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
  result = getJSON(response)
  return result

def get_stored_metadata():
  with open(json_path) as infile:
    result = getJSON(infile)
    return result

# def write_current_metadata():
#   with open(json_path, 'a') as f:
#     response = urllib2.urlopen(url)
#     #json.dump(response, f)
#     #f.write(str(response))
#     f.write("this is a test")
    
    
    
    
###############################################################################    
# Main Function
def main ():

  current_metadata = get_current_metadata()
  current_id = current_metadata["id"]
  print current_id
  
  stored_metadata = get_stored_metadata()
  stored_id = stored_metadata["id"]
  print stored_id
  
# compare the values
#   if (current_id == stored_id):
#     print ('OK!')
#   else:
#     print ('Something is wrong!')
#     write_current_metadata()

# Call main()
if __name__ == '__main__':
  main()