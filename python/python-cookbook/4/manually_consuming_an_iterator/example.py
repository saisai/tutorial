
"""
Problem
You need to process items in an iterable, but for whatever reason, you can’t or don’t want
to use a for loop.
"""

with open('/etc/passwd') as f:
    try:
        while  True:
            #line = next(f)
            line = next(f, None)
            if line is None:
                break
            print(line, end='')
    except StopIteration:
        pass
