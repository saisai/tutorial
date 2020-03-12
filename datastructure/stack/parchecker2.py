from stack import Stack

"""
https://runestone.academy/runestone/books/published/pythonds/BasicDS/BalancedSymbolsAGeneralCase.html
"""

def matches(open,close):
    #print(open, close)
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)
    
def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        #print(symbol)
        if symbol in "([{":
            #print(symbol, 'again')
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                #print(top)
                if not matches(top,symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False




print(parChecker2('{({([][])}())}'))
print(parChecker2('[{()]'))

'''
def parChecker(symbolString):

    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(opener, closer):
    print(opener, closer)
    opens = "([{"
    closers = ")]}"

    return opens.index(opener) == closers.index(closer)

print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))
'''