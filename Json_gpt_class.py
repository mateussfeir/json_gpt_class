import json

# Creating any data just to study how to save it using json

dictionary = {
    'name' : 'Mateus',
    'age' : 28,
    'city' : 'Toronto'
}

print(f'Python data: {dictionary}\n')

# Using json.dumps we are dumping our data and converting it to json format

json_data = json.dumps(dictionary)

print(f'Json data: {json_data}\n')

''' We can tell when we are printing the data that the only difference so far is that
Json string is outputting double quotes by default.'''

# To convert our data from json format back to normal python object string we need to use json.loads

data = json.loads(json_data)

print(f'Converting back to Python data: {data}\n')

with open('data.json', 'w') as f:
    json_data = json.dump(data, f)
    print('Data was successfully saved')

print(json_data)

with open('data.json', 'r') as f:
    reading_json_data = json.load(f)
print(reading_json_data)
