import sys


def mask_judge(mask):
    # 判断子网掩码
    res = ""
    for m in mask:
        try:
            m = int(m)
        except:
            return False

        if m > 255 or m < 0:
            return False
        binary_string = bin(m)[2:]
        binary_string = "0" * (8-len(binary_string)) + binary_string
        res += binary_string

    if '01' in res or '0' not in res:
        return False
    return True


def ip_judge(ip):
    for i in ip:
        try:
            i = int(i)
        except:
            return False

        if i > 255 or i < 0:
            return False
    return True


def ip_c(ip):
    if 0 <= int(ip[0]) < 127:
        return "A"
    elif 128 <= int(ip[0]) < 192:
        return "B"
    elif 192 <= int(ip[0]) < 224:
        return "C"
    elif 224 <= int(ip[0]) < 240:
        return "D"
    elif 240 <= int(ip[0]) < 256:
        return "E"


def ip_private(ip):
    if ip[0] == "10":
        return True
    if ip[0] == "172" and 16 <= int(ip[1]) <= 31:
        return True
    if ip[0] == "192" and ip[1] == "168":
        return True
    return False


if __name__ == '__main__':
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    error = 0
    private = 0

    for line in sys.stdin:
        line = line.split('~')
        ip, mask = line[0], line[1]
        ip = ip.split('.')
        mask = mask.split('.')
        if ip[0] == "127" or ip[0] == "0":
            continue

        if not mask_judge(mask):
            error += 1
            continue

        if not ip_judge(ip):
            error += 1
            continue

        category = ip_c(ip)

        if category == "A":
            A += 1
        elif category == "B":
            B += 1
        elif category == "C":
            C += 1
        elif category == "D":
            D += 1
        elif category == "E":
            E += 1

        if ip_private(ip):
            private += 1

    print(A, B, C, D, E, error, private)
