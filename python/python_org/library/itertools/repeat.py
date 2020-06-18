
# Python code to demonstrate the working of
# repeat()


import itertools

# using repeat() to repeatedly print string
print(list(map(str.upper,
               itertools.repeat('geeksforgeeks', 3))))


# https://www.geeksforgeeks.org/python-itertools-repeat
