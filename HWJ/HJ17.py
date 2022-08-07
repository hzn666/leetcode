if __name__ == '__main__':
    res = [0, 0]

    coordinate_list = input().split(";")

    for c in coordinate_list:
        if len(c) > 3:
            continue
        try:
            direction = c[0]
            distance = int(c[1:])
        except:
            continue
        if direction == 'A':
            index = (0, -1)
        elif direction == 'D':
            index = (0, 1)
        elif direction == 'W':
            index = (1, 1)
        elif direction == 'S':
            index = (1, -1)
        else:
            continue

        res[index[0]] += index[1] * distance

    print(res[0], res[1], sep=',')
