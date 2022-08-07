import collections

if __name__ == '__main__':
    string = input().lower()
    c = input().lower()

    dic = collections.defaultdict(int)

    for _ in string:
        dic[_] += 1

    print(dic[c])

