import CountrySpecificVariablesUtls
import json

print("Starting Up")
# Only loads what we need
CountrySpecificVariablesUtls.load()
print("Loading is done")

allRecords = CountrySpecificVariablesUtls.getAllCountrySpecificVariablesRecords()

dic = {}

for record in allRecords:
    if record.iso_code.lower() not in dic.keys():
        dic[record.iso_code.lower()] = record.human_development_index

print(dic)
with open("data.json", "w") as outfile:
    json.dump(dic, outfile)

# Opening JSON file
f = open('data.json')
data = json.load(f)
f.close()