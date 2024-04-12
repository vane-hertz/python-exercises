'''Without running the following code, what do you think it will do?
'''

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

'''It will error out as the third parameter does not have a 
default value while the parameter before it, second, has a
default value.
'''