from functools import partial
with open('vocabulary.txt', 'r') as f:
    for block in iter(partial(f.read, 64), ''):
        print(block)
