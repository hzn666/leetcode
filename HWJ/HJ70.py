n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

order = input()
res = 0
stack = []

for c in order:
    if c.isalpha():
        stack.append(matrix[ord(c) - ord('A')])
    else:
        stack.append(c)

order = stack
stack = []

for c in order:
    if c == ')':
        y = stack.pop()
        x = stack.pop()
        res += x[0] * x[1] * y[1]
        stack.pop()
        stack.append([x[0], y[1]])
    else:
        stack.append(c)

print(res)
