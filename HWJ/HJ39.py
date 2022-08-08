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
        binary_string = "0" * (8 - len(binary_string)) + binary_string
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


while True:
    try:
        mask = input().split('.')
        ip1 = input().split('.')
        ip2 = input().split('.')

        if not mask_judge(mask) or not ip_judge(ip1) or not ip_judge(ip2):
            print(1)
            break

        for i in range(4):
            if int(ip1[i]) & int(mask[i]) != int(ip2[i]) & int(mask[i]):
                print(2)
                break
        else:
            print(0)

    except:
        break
