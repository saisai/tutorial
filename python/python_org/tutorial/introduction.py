

print("""\
Usage: thingy [OPTIONS]
    -h          Display this usage message
    -H hostname Hostname to connect to

""")

print()

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')
print(40 * '-' + 'end')
print()

print("Py" "thon")
print()

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print()

'''
Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
'''
word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5
print()

print(word[-1]) # last[]character
print(word[-2]) # second-last character
print()

#Note that since -0 is the same as 0, negative indices start from -1.

print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[2:5]) # characters from position 2 (included) to 5 (excluded)
print()
# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

print(word[:2] + word[2:])
print(word[:4] + word[4:])

print()
# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[4:]) # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end


# https://docs.python.org/3/tutorial/introduction.html