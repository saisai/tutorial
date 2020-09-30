'''

https://www.techiedelight.com/check-given-expression-balanced-expression-not/
'''
from collections import deque


# function to check if given expression is balanced or not

def balance_parenthesis(exp):

    # base case: length of the expression must be even
    if len(exp) & 1:
        return False

    # take an empty stack of characaters
    stack = deque()

    # traverse the input expression
    for ch in exp:

        # if current in the epxression is an opening brace,
        # push it to the stack
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)

        # if current in the expression is a clsoing brace
        if ch == ')' or ch == ']' or ch == '}':
            # return false if mismatch is found (i.e. if stack is empty,
            # the number of opening braces is less than number of closing
            # brace, so expression cannot be balanced)
            if not stack:
                return False

            # pop character from the stack
            top = stack.pop()


            # it the topped characeter if not an opening brace or does not
            # pair with current character of the expression
            if (top == '(' and ch != ')') or (top == '{' and ch != '}') \
                    or (top == '[' and ch != ']'):
                return False


    # expression is balanced only if sack is empty at this point
    return not stack

if __name__ == '__main__':
    exp = "{()}[{}]"

    print(balance_parenthesis(exp))




