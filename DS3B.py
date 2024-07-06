#3B-Write a program to convert an infix expression to postfix and prefix conversion.
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = ''
    
    for char in expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                postfix += stack.pop()
            stack.append(char)
    
    while stack:
        postfix += stack.pop()
    
    return postfix

def infix_to_prefix(expression):
    expression = expression[::-1]
    for i in range(len(expression)):
        if expression[i] == '(':
            expression = expression[:i] + ')' + expression[i+1:]
        elif expression[i] == ')':
            expression = expression[:i] + '(' + expression[i+1:]
    
    postfix_expression = infix_to_postfix(expression)
    prefix_expression = postfix_expression[::-1]
    
    return prefix_expression

infix_expression = "a+b*c-(d/e+f)*g"
postfix_result = infix_to_postfix(infix_expression)
prefix_result = infix_to_prefix(infix_expression)

print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_result)
print("Prefix Expression:", prefix_result)
