if __name__ == '__main__':
    string = list(input())[::-1]
    res = []
    for i in string:
        if i not in res:
            res.append(i)

    print(int("".join(res)))