import requests
import asyncio

data_json: str

with open('request_json.txt', 'r') as file:
    data_json = file.read()

d = requests.post('http://localhost:8080/', data=data_json)
print(d.status_code, d.reason, d.content)
d = requests.post('http://localhost:8080/', data={})
print(d.status_code, d.reason, d.content)
