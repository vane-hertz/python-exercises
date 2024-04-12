'''Without running the following code, what do you think it will do?
'''
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

'''It will error out as not enough arguments were passed to
the foo function; expected at least one argument
'''