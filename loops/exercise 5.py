my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for lst in my_list:
    for item in lst:
        if item % 2 == 0:
            print(item)