set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)
'''Without running this code, what will it print? Why?

It will print 
{('a', 'b', 'c'), 'Monty Python', 42, range(5, 10)}
'''