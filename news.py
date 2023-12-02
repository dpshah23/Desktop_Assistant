import requests
import json
from datetime import datetime, timedelta
from speak import speak
current_date = datetime.now()
one_day_before = current_date - timedelta(days=2)
def news(search):
        data=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category={search}&from={one_day_before}&sortBy=publishedAt&apiKey=4e339f9aa0a24bba8e1c7e7dc1926a7e').text
        news=json.loads(data)
        speak("here is first news")
        arts=news['articles']
        for articles in arts:
                article=articles['title']
                desc=articles['description']
                print(article)
                print(desc)

                speak(article)
                if len(desc)<=200:
                        speak(desc)

                else:
                        pass
                news_url=articles["url"]
                print(f"For more info refer {news_url}")

                a=int(input("press 1 to continue and press 2 to stop: "))
                if a==1:
                       pass
                elif a==2:
                        break
                else:
                        speak("invalid input")

   

