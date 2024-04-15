age = int(input('How old are you? '))

print(f'You are {age} years old.')

for increment in range(10, 50, 10):
    print(f'In {increment} years, you will be {age + increment} years old.')