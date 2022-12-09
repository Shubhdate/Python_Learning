#JSON File operation - 
#used in web developnment for sending msg to client from server side
# json objects       dict{"key":"value"}
# numbers 10 10.55   int float  
# array [10,"string"]  list
#      tuple
#" "     '' ""  """ ""

import json
handle = open("json.json","r")
content = handle.read()
print(content)

#convert json into python
import json
handle = open("json.json","r")
content = handle.read()
d = json.loads(content)
print(d)

d = json.loads(content)
print(d['dependencies'])

