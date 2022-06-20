from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for i in range(len(tokens)):
        if tokens[i] not in ['+', '-', '*', '/']:
            stack.append(tokens[i])
        else:
            b = int(stack.pop())
            a = int(stack.pop())

            if tokens[i] == '+':
                result = a + b
            elif tokens[i] == '-':
                result = a - b
            elif tokens[i] == '*':
                result = a * b
            else:
                result = a / b
            stack.append(result)

    return int(stack[0])

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))