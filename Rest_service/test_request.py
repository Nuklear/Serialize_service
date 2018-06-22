import requests
import asyncio
import json

data_json: str

with open('request_json.txt', 'r') as file:
    data_json = file.read()

d = requests.post('http://localhost:8080/', data=data_json)
print(d.status_code, d.reason, d.content)
d = requests.post('http://localhost:8080/', data={})
print(d.status_code, d.reason, d.content)

# dict_json = json.loads(data_json)
#
# char_id = [i['characteristicId'] for i in dict_json["measurementTask"]['characteristics']]
# print(char_id)
# print('-' * 50)
# data = dict_json.get('experimentType1Data').get('table')
# for d in data:
#     if d.get('characteristicId') == '03816e06-d7cd-4d2c-8632-6ce33cedf788':
#         print([i.get('value') for i in d.get('cells')])
#
# data_dict = {}
# data = dict_json.get('measurementTask').get('characteristics')
# for d in data:
#     if d.get('characteristicId') == '03816e06-d7cd-4d2c-8632-6ce33cedf788':
#         data_dict['nominal_dimmen'] = d.get('nominalValue')
#         data_dict['upper_dev_limit'] = d.get('upperProcessLimit').get('value')
#         data_dict['lower_dev_limit'] = d.get('lowerProcessLimit').get('value')
#
# data = dict_json.get('measurementSystem').get('characteristics')
# for d in data:
#     if d.get('characteristicId') == '03816e06-d7cd-4d2c-8632-6ce33cedf788':
#         data_dict['resolution'] = d.get('resolution')
#
# print('-/-'*30)
# print(data_dict)