'''In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.
'''

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

'''function names: multiply line 1, get_num line 4, print line 10
float line 5, input line 5
parameters: left, right line 1 prompt line 4
'''