import requests

url = 'https://www.buda.com/api/v2/markets/'
response = requests.get(url+'btc-clp')
print(response.json())