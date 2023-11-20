import requests
import speak as sp
import json
def joke():

    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'PLulNToKMBLLsdbCLIZb4w==5CkjXhZn6YtT7rz7'})
    if response.status_code == requests.codes.ok:
    
        data = json.loads(response.text)
        joke=data[0]['joke']
        print(joke)

        sp.speak(joke)
    else:
        print("Error:", response.status_code, response.text)