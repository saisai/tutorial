def hello(*args):

    def do_add():

        x, y = args
        return x + y


    return do_add


print(hello(2, 3)())



def hello2(*args):

    def do_add(a):
        print(args)
        def hello():
            print(args)
            x, y = args 
            return x + y + a
            
        return hello


    return do_add


print(hello2(2, 3)(1)())


def hello3(*args):

    def do_add(a):
        print(args)
        def hello(b):
            print(args)
            x, y = args 
            return x + y + a + b
            
        return hello


    return do_add


print(hello3(2, 3)(1)(2))
