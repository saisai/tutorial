def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.append(symbol)
        else:
            if s == []:
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s == []:
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('((())'))
