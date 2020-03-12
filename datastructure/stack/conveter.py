
from stack import Stack

def divideBy2(decNumber):

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        print(rem)
        remstack.push(rem)
        decNumber = decNumber // 2
        print(decNumber, 'a')
    
    print('size', remstack.size())
    print(remstack)
    print(list(remstack))
    
    #for a in remstack:
        #print(a)
    
    binString = ""
    while not remstack.isEmpty():        
        binString = binString + str(remstack.pop())

    return binString
    
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % base 
        remstack.push(rem)
        decNumber = decNumber // base 
        
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
        
    return newString
        

if __name__ == '__main__':
    print(divideBy2(42))
    print(baseConverter(25,2))
    print(baseConverter(25,16))
