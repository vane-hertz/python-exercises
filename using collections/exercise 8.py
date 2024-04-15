'''Explain why the code below prints different values on lines 3 and 4.
'''

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

'''It prints different values because the rfind on line 3
is operating on a slice of a string, and uses an index based
on that slice, while the rfind on line 4 is using an index
based on the whole string while told to look in the slice.
'''