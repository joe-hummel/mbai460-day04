#
# Calls MovieLens web service hosted in AWS.
#
# Prof. Joe Hummel
# Northwestern University
#

import requests
from configparser import ConfigParser

print("**Starting**")
print()

#
# setup AWS based on config file:
#
print(">>reading config file...")

config_file = 'movielens-config.ini'    
configur = ConfigParser()
configur.read(config_file)

#
# get web service URL from config file:
#
endpoint = configur.get('webservice', 'endpoint')

#
# call the web service to retreive movies:
#
print(">>calling web service...")
print(endpoint)

url = endpoint + "/movies"

response = requests.get(url)

status_code = response.status_code

print()
print(status_code)
print()

body = response.json()

if status_code == 200: # success!
  for row in body:
    print(row)
else: # error:
  print("**Error:", body)

print()
print("**Done**")
