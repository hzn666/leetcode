from typing import List


def isStraight(nums: List[int]) -> bool:
    repeat = set()

    mi = 14
    ma = 0

    for num in nums:
        if num == 0:
            continue
        ma = max(ma, num)
        mi = min(mi, num)
        if num in repeat:
            return False
        repeat.add(num)
    return ma - mi < 5