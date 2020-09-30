import collections


c = collections.Counter('abcdaaab')

for letter in 'abcdef':
    print('{} : {}'.format(letter, c[letter]))
