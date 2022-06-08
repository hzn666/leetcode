from typing import List


def calSum(piles, k):
    sum = 0
    for pile in piles:
        sum -= (pile + k - 1) // k
    return sum


def minEatingSpeed(piles: List[int], h: int) -> int:
    maxValue = max(piles)

    left, right = 1, maxValue

    while left <= right:
        mid = left + (right - left) // 2

        if calSum(piles, mid) < -h:
            left = mid + 1
        else:
            right = mid - 1

    return left


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h), calSum(piles, minEatingSpeed(piles, h)))
k_list = []
for k in range(1, 12):
    k_list.append(calSum(piles, k))
print(k_list)
