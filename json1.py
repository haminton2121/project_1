import json
from pprint import pprint # pretty print
a1 = """
{"employee": [
{ "name" : "nguyen xuan hoa" ,
  "email": "haminton212@gmail.com",
  "address": "256 ss street"},
{ "name" : "nguyen xuan hoa 1" ,
  "email": "haminton212@gmail1.com",
  "address": "2561 ss street"}
]}"""
data1 = json.loads(a1)
pprint(data1)