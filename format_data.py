import json

with open('round1/round1/final.json', 'r',encoding='utf-8') as file:
    data = json.load(file)

formatted_data = []

for item in data:
    formatted_item = {}
    formatted_item['data'] = [x.replace('\n', '').replace(' ', '') for x in item['data']]
    formatted_data.append(formatted_item)

with open('formatted_final.json', 'w') as file:
    json.dump(formatted_data, file)