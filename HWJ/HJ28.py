def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find(odd, visited, choose, evens):
    for j, even in enumerate(evens):
        if isPrime(odd + even) and not visited[j]:
            visited[j] = True
            if choose[j] == 0 or find(choose[j], visited, choose, evens):
                choose[j] = odd
                return True
    return False


n = input()
num = list(map(int, input().split()))

evens = []
odds = []

for i in num:
    if i % 2:
        odds.append(i)
    else:
        evens.append(i)

choose = [0] * len(evens)
count = 0

for odd in odds:
    visited = [False] * len(evens)
    if find(odd, visited, choose, evens):
        count += 1
