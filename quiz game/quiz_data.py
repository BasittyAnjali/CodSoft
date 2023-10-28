import requests

parameters = {
    "amount": 20,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]