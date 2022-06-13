from typing import List


def heightChecker(heights: List[int]) -> int:
    sort = sorted(heights)

    result = [0 if a == b else 1 for a, b in zip(heights, sort)]

    return sum(result)


heights = [1, 1, 4, 2, 1, 3]
print(heightChecker(heights))
