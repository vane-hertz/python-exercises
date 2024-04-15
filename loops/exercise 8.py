my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = {f'{string}': len(string) for string in my_set if len(string) % 2 != 0}
print(result)