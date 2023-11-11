import requests
def exchange(val,base,target):
    api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={target}&have={base}&amount={val}'
    data=requests.get(api_url,headers={'X-Api-key':'PLulNToKMBLLsdbCLIZb4w==5CkjXhZn6YtT7rz7'})
    print(data.text)

exchange(1000,'inr','aud')

    