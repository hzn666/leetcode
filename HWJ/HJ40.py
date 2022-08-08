alpha = 0
space = 0
number = 0
other = 0

a = input()

for i in a:
    if ord('0') <= ord(i) <= ord('9'):
        number += 1
    elif i.isalpha():
        alpha += 1
    elif i == " ":
        space += 1
    else:
        other += 1

print(alpha)
print(space)
print(number)
print(other)
