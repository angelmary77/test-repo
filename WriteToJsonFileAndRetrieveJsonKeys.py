import json

def readJsonFile(fileName):
    Names = []
    Dept = []
    with open(fileName, 'r') as json_file:
        data = json.load(json_file)

        for p in data["People"]:
            name =  "name: " + p["name"]
            Names.append(name)
            dep = "Department: " + p["dep"]
            Dept.append(dep)

    return Names, Dept

data = {}
data["People"] = []
data["People"].append({"name":"mary",
                       "empID" : "RI420",
                       "dep": "SB",
                       "location": "chennai"})
data["People"].append({"name":"Angel",
                       "empID" : "RI421",
                       "dep": "HR",
                       "location": "Mumbai"})
data["People"].append({"name":"Thanya",
                       "empID" : "xyx",
                       "dep": "Student",
                       "location": "US"})

with open("Test.json", 'w+') as outputfile:
    data = json.dump(data, outputfile)

# with open("Test.json", 'r') as fl:
#     f = json.load(fl)
#     for p in f['People']:
#         print p['name']



Name = readJsonFile("Test.json")
print Name

# print data
# print data["People"]


