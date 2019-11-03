import requests
import json

url = ("http://jservice.io/api/clues?offset=")
id = 0
comp_dates = []
comp_question = []
comp_answer = []

'''
Use a changing url and offset to access all 
of the api's data. Did this to compensate for
technical issues with my computer and 
bundle install.
'''

# Loop through pages of api and add to list of dicts
while id < 156709: #156709
    if(id % 1000 == 0): print(id)
    dates = []
    question = []
    answer = []
    response = requests.get(url + str(id))

    dates = json.loads(response.text)
    question = json.loads(response.text)
    answer = json.loads(response.text)

    for i in range(0, len(dates)):
        # Deletes for dates
        del dates[i]["answer"]
        del dates[i]["question"]
        del dates[i]["value"]
        del dates[i]["category_id"]
        del dates[i]["created_at"]
        del dates[i]["updated_at"]
        del dates[i]["game_id"]
        del dates[i]["invalid_count"]
        del dates[i]["category"]
        comp_dates.append(dates[i])
        # Deletes for question
        del question[i]["answer"]
        del question[i]["airdate"]
        del question[i]["value"]
        del question[i]["category_id"]
        del question[i]["created_at"]
        del question[i]["updated_at"]
        del question[i]["game_id"]
        del question[i]["invalid_count"]
        del question[i]["category"]
        comp_question.append(question[i])
        # Deletes for Answer
        del answer[i]["question"]
        del answer[i]["airdate"]
        del answer[i]["value"]
        del answer[i]["created_at"]
        del answer[i]["category_id"]
        del answer[i]["updated_at"]
        del answer[i]["game_id"]
        del answer[i]["invalid_count"]
        del answer[i]["category"]
        comp_answer.append(answer[i])

    id += 100
        


# Create a file for our new list of dictionaries
with open('dates.json', 'w') as f:
        json.dump(comp_dates, f)

with open('question.json', 'w') as f:
        json.dump(comp_question, f)

with open('answer.json', 'w') as f:
        json.dump(comp_answer, f)
