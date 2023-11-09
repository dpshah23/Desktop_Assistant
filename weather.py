import requests
def weather(city):
    data=requests.get(f"http://api.weatherapi.com/v1/current.json?key=4da0e8341db549c0b6c163519231608&q={city}&aqi=yes")
    location=data.json()['location']['name']
    temp=data.json()['current']['temp_f']   
    condition1=data.json()['current']['condition']['text']
    c = (temp - 32) * 5 / 9
    list1=[]
    list1.append(location)
    list1.append(condition1)
    list1.append(c)

    return list1

    