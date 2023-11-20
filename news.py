import requests
def news(search):
        data=requests.get(f'https://newsapi.org/v2/everything?q={search}&from=2023-11-14&sortBy=publishedAt&apiKey=4e339f9aa0a24bba8e1c7e7dc1926a7e')
        print(data.text)
   

news('technology')