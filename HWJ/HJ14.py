if __name__ == '__main__':
    num = int(input())
    res = []
    for _ in range(num):
        res.append(input())
    for _ in sorted(res):
        print(_)