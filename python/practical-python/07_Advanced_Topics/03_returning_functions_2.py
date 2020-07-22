# delayed evaluation

import time

def after(seconds, func):
    time.sleep(seconds)
    func()

def greeting():
    print("hello word")

after(3, greeting)


def add(x, y):
    def do_add():
        print('fAdding {x} + {y} -> {x+y}')
    return do_add

c = after(3, add(2, 3))
