
from arraystack import ArrayStack

def reverse_file(filename):
    """
    Overwrite given file with its contents line-by-line reversed.
    """
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n')) # we will re-insert newlines when writing
    original.close()


    # now we over write with contents in LIFO order
    output = open(filename, 'w') # reopening file overwrites orignal
    while not S.is_empty():
        output.write(S.pop() + '\n') # re-insert newline characters
    output.close()


if __name__ == '__main__':

    reverse_file('test.py')
