import json
from pprint import pprint

data = {
    "SlNo" : "1",
    "Name" : "Mary",
    "EMPID" : "RI420",
    "Department" : "Software"
}

json_str = json.dumps(data, indent=5)
print json_str
# pprint (json_str)
print data["Name"]

with open('Test.json', 'w+') as f:
    json.dump(data, f)

with open('Test.json', 'r') as f:
    print json.load(f)