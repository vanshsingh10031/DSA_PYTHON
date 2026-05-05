def infix_to_postfix(expression):
    stack = []
    output = []

    # precedence of operators
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    tokens = expression.split()

    for token in tokens:
        # if operand → add to output
        if token.isdigit():
            output.append(token)

        # if '(' → push
        elif token == '(':
            stack.append(token)

        # if ')' → pop until '('
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('

        # operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())

            stack.append(token)

    # pop remaining operators
    while stack:
        output.append(stack.pop())

    return " ".join(output)

expr = "( 3 + 4 ) * 2 - 7"
result = infix_to_postfix(expr)
print(result)