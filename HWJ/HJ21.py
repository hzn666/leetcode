string = input()
res = ""

dic = {

}

for i in string:
    if ord('A') <= ord(i) < ord('Z'):
        res += chr(ord(i) + 1).lower()
    elif ord(i) == ord('Z'):
        res += 'a'
    elif ord('a') <= ord(i) <= ord('c'):
        res += '2'
    elif ord('d') <= ord(i) <= ord('f'):
        res += '3'
    elif ord('g') <= ord(i) <= ord('i'):
        res += '4'
    elif ord('j') <= ord(i) <= ord('l'):
        res += '5'
    elif ord('m') <= ord(i) <= ord('o'):
        res += '6'
    elif ord('p') <= ord(i) <= ord('s'):
        res += '7'
    elif ord('t') <= ord(i) <= ord('v'):
        res += '8'
    elif ord('w') <= ord(i) <= ord('z'):
        res += '9'
    else:
        res += i

print(res)
