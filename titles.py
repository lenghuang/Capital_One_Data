import requests
import json

url = ("http://jservice.io/api/category?id=")
id = 1
final_data = []

# Initially create a file of all the categories in the API
# compiled. Then delete entries that took up too much data.
# This can be used to then search for things in a quicker way.
# This allow checks for faults in the API where there are
# null entries. 

# Loop through pages of api and add to list of dicts
while(id < 18419):
    initial_data = []
    response = requests.get(url + str(id))
    initial_data.append(json.loads(response.text))
    # Skip null ID
    if (len(initial_data[0].keys()) > 2):
        del initial_data[0]["clues_count"]   
        del initial_data[0]["clues"]
        final_data.append(initial_data[0])
    id += 1

# Create a file for our new list of dictionaries
with open('comp.json', 'w') as f:
        json.dump(final_data, f)