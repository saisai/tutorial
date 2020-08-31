
def divideBy2(decNumber):

    remstack = []

    while decNumber > 0:
        rem = decNumber % 2
        remstack.append(rem)
        decNumber =decNumber // 2

    binString = ""
    while not remstack == []:
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))
print(divideBy2(30000))


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = []

    while decNumber > 0:
        rem = decNumber % base
        remstack.append(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack == []:
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))
# https://runestone.academy/runestone/books/published/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
