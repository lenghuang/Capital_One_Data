import requests
import json

url = ("http://jservice.io/api/category?id=")
id = 1
final_data = []

'''
Use a changing url and offset to access all 
of the api's data. Did this to compensate for
technical issues with my computer and 
bundle install.
'''

# Loop through pages of api and add to list of dicts
while(id < 18419): #14280 #156709 #18418
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
with open('titles_new.json', 'w') as f:
        json.dump(final_data, f)