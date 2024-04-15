'''The following code causes an infinite loop (a loop that never stops iterating). Why?
'''

counter = 0

while counter < 5:
    print(counter)

'''Because counter is never incremented or altered while
being the condition for the while loop.
'''