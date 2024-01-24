import requests

url = 'http://127.0.0.1:8000/api/items/'
headers = {'Authorization': '75de936f9e77cc0e1981cf31a34258f4f3ab28e8'}

response = requests.get(url, headers=headers)
print(response.json())
