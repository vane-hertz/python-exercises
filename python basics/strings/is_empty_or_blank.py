def is_empty_or_blank(str):
    str = str.strip(' ')
    return not str

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True