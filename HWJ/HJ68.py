while True:
    try:
        n = int(input())
        order = int(input())

        ls = []
        for i in range(n):
            name, grade = input().split()
            ls.append((name, int(grade)))
        ls.sort(key=lambda x: x[1], reverse=order == 0)
        for i in ls:
            print(*i)
    except:
        break
