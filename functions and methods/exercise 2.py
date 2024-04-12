'''
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

What does this program print? Why?

It prints 'bar' as 'qux' is in local scope, outside of the prints global scope
'''