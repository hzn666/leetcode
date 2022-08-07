if __name__ == '__main__':
    num = int(input())

    dic = {}

    for _ in range(num):
        k, v = list(map(int, input().split()))
        if k in dic:
            dic[k] += v
        else:
            dic[k] = v

    for k in sorted(dic):
        print(k, dic[k])