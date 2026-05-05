import array as arr

def push(stack, value):
    stack.append(value)

expression = "3 4 2 * 7 - 2 3 * +"
bachiket = expression.split()

stack = []

for val in bachiket:
    if val.isdigit():
        push(stack, int(val))
    else:
        b = stack.pop()
        a = stack.pop()

        if val == '+':
            push(stack, a + b)
        elif val == '-':
            push(stack, a - b)
        elif val == '*':
            push(stack, a * b)
        elif val == '/':
            push(stack, a // b)

print(stack[0])

print(a)