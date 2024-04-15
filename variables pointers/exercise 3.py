dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

'''Without running this code, what will it print? Why?

The Life of Brian because dict() creates a new dict that is not stored
at the same pointer as dict1
'''