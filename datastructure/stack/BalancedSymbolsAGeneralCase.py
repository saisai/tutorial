
def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.append(symbol)
        else:
            if s == []:
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s == []:
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))

# https://runestone.academy/runestone/books/published/pythonds/BasicDS/BalancedSymbolsAGeneralCase.html
