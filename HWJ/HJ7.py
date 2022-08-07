if __name__ == '__main__':
    num = float(input())
    floor = int(num)

    if num - floor >= 0.5:
        print(floor + 1)
    else:
        print(floor)
