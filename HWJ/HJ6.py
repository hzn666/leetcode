if __name__ == '__main__':
    num = int(input())

    for i in range(2, int(num ** 0.5) + 1):
        while not num % i:
            print(i, end=" ")
            num //= i

    if num > 2:
        print(num)