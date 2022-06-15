def isHappy(n: int) -> bool:
    def calculate(num):
        result = 0

        while num:
            result += (num % 10) ** 2
            num = num // 10

        return result

    record = set()

    while True:
        n = calculate(n)
        if n == 1:
            return True

        if n in record:
            return False
        else:
            record.add(n)


n = 19
print(isHappy(n))
