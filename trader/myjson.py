import json

data ={
        'name' : 'ACME',
        'shares' : 100,
        'price' : 542.23
        }
json_str = json.dumps(data)

mydata = json.loads('{"price": 542.23, "shares": 100, "name": "ACME"}')

print(mydata['price'])
