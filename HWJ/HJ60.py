def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


n = int(input())

for i in range(n // 2, n):
    if isPrime(i) and isPrime(n - i):
        print(n - i)
        print(i)
        break
