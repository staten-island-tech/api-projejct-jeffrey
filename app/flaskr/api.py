import requests
api_url="https://fortnite-api.com/v2/cosmetics/br"
response = requests.get(api_url)
response.json() 
print(response.text)