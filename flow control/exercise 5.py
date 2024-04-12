'''What does this code output, and why?
'''

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

'''It prints Empty because an empty list is falsey.
'''