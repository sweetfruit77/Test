import json

with open('jsontest/data.json',encoding = 'UTF8') as f:
    data = json.load(f)
print(type(data))
print(data)