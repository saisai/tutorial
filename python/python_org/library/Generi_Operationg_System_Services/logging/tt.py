import os
filename = 'test.py'
if filename and os.path.isfile(filename):
    print('test')
    with open(filename) as fobj:
        startup_file = fobj.read()
        print(startup_file)
    exec(startup_file)
