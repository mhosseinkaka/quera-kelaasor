
def check(sign1,sign2):
    if sign1 == '[' and sign2 == ']':
        return True
    elif sign1 == '{' and sign2 == '}':
        return True
    elif sign1 == '(' and sign2 == ')':
        return True
    else:
        return False


def is_a_True(list_sign):
    stack = []
    for char in list_sign:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if not stack:
                return False
            char_stack = stack.pop()
            if not check(char_stack, char):
                return False
    return not stack 

list_sign = list(input())
print(is_a_True(list_sign))



