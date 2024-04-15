dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

'''Without running this code, what will it print? Why?

[1, 42, 3] although dict2 is assigned a new dict object the two 
unique dicts still reference the same list which has its own pointer
the two dicts reference the same list so changes done to the list would reflect in both dicts.
'''