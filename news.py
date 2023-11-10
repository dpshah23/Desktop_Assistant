import requests
def news(search):
        data=requests.get(f'https://newsdata.io/api/1/archive?apikey=pub_32671c056c8e6522b35c361f4bd4b21403353&q=example&language=en&from_date=2023-01-19&to_date=2023-01-25')
        print(data.json())
   

news('technology')