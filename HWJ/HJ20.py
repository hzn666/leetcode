string = input()
res = True
if len(string) <= 8:
    res = False

a, b, c, d = 0, 0, 0, 0

for s in string:
    if ord('a') <= ord(s) <= ord('z'):
        a = 1
    elif ord('A') <= ord(s) <= ord('Z'):
        b = 1
    elif ord('0') <= ord(s) <= ord('9'):
        c = 1
    else:
        d = 1

if a + b + c + d < 3:
    res = False

for i in range(len(string) - 3):
    if len(string.split(string[i:i + 3])) >= 3:
        res = False

print('OK') if res else print('NG')
