my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = []
for item in my_list:
    if item % 2 == 0:
        result.append('even')
    elif item % 2 != 0:
        result.append('odd')
print(result)