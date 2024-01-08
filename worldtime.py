import requests
import speak as sp
def worldtime(city):
    api_url = f'https://api.api-ninjas.com/v1/worldtime?city={city}'
    data1=requests.get(api_url,headers={'X-Api-Key':'PLulNToKMBLLsdbCLIZb4w==5CkjXhZn6YtT7rz7'})
    data=data1.json()
    sp.speak(f" location : {city}  date : {data['date']} and time : {data['hour']} o'clock {data['minute']} minutes day : {data['day_of_week']}")

