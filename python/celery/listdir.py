import os
import sys


def count_py_files_in_repo(dirname):
    if os.path.exists(os.path.join(dirname, '.git')):
        print(dirname)
        count = 0
        for root, dirs, files in os.walk(dirname):
            count += len([f for f in files if f.endswith('.py')])
        print('{} has {} Python files'.format(dirname, count))

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            count_py_files_in_repo(path)


count_py_files_in_repo('/home/snp/www/tutorial/')

