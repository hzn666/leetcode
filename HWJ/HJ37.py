a = 1
b = 1

n = int(input())

if n < 3:
    print(1)

for i in range(n - 2):
    a, b = b, a + b
print(b)
