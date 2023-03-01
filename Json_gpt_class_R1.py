import json

''' JSON is a abbreviation of JavaScript Object Notation'''

# That is out data about adaptors 

ac_adaptors = {'Adaptors': [
    {
    'Watts' : '65W',
    'External diameter' : '5.5mm',
    'Internal diameter' : '1.7mm',
    'Amper' : '3.42A'
},
{
    'Watts' : '35W',
    'External diameter' : '4mm',
    'Internal diameter' : '1.5mm',
    'Amper' : '2.1A'
}
]}
print('\nRaw data:')
print(ac_adaptors)
print(type(ac_adaptors))


with open('Json_data.txt', mode ='w') as f:

    # Step 1: Convert the data from a python dictionary to a JSON string:

    json_data = json.dumps(ac_adaptors)

    print('\nAfter JSON dump:')
    print(json_data)
    print(type(json_data))
    # f.write(json_data) We need to use this code just in case if you want to see the data written in the text file as normal letters
    
    # Step 2: Convert a JSON string to a python dictionary:

    json_back = json.loads(json_data)
    print('\nAfter JSON load:')
    print(json_back)
    print(type(json_back))

# Step 3: play with the data as a normal python dictionary just to be sure that it's working as it is supposed to

for inf in json_back['Adaptors']:
    print(inf['Watts'])

# So we can take a string and convert to a dictionary using json.loads that is useful
