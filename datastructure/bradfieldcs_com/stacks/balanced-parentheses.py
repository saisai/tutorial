OPENING = '('

def is_balanced(parentheses):
    stack = []
    for paren in parentheses:
        if paren == OPENING:
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError: # too many closing parens
                return False
    return len(stack) == 0 # False if too many opening parens


if __name__ == '__main__':
    print(is_balanced('(((())))'))
    print(is_balanced('(())'))
    print(is_balanced('(()'))
