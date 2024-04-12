def number_range(num):
    if num >= 0 and num <= 50:
        print(f'{num} is between 0 and 50')
    elif num >= 51 and num <= 100:
        print(f'{num} is between 51 and 100')
    elif num > 100:
        print(f'{num} is greater than 100')
    else num < 0:
        print(f'{num} is less than 0')            