import requests
api_url="https://www.amiiboapi.com/api/amiibo/"
response = requests.get(api_url)
response.json() 
api=response.text
print(api)