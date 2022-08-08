def encode(n):
    res = ""
    for i in n:
        if i.isalpha():
            if ord('a') <= ord(i) < ord('z'):
                res += chr(ord(i) + 1).upper()
            elif ord('A') <= ord(i) < ord('Z'):
                res += chr(ord(i) + 1).lower()
            elif ord(i) == ord('z'):
                res += "A"
            elif ord(i) == ord('Z'):
                res += "a"
        elif ord('0') <= ord(i) < ord('9'):
            res += chr(ord(i) + 1)
        elif ord(i) == ord('9'):
            res += "0"
    return res


def decode(n):
    res = ""
    for i in n:
        if i.isalpha():
            if ord('a') < ord(i) <= ord('z'):
                res += chr(ord(i) - 1).upper()
            elif ord('A') < ord(i) <= ord('Z'):
                res += chr(ord(i) - 1).lower()
            elif ord(i) == ord('a'):
                res += "Z"
            elif ord(i) == ord('A'):
                res += "z"
        elif ord('0') < ord(i) <= ord('9'):
            res += chr(ord(i) - 1)
        elif ord(i) == ord('0'):
            res += "9"
    return res


a = input()
print(encode(a))
b = input()
print(decode(b))
