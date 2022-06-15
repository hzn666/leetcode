import collections
from typing import List


def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    record = collections.defaultdict(int)
    count = 0

    for i in nums1:
        for j in nums2:
            record[i + j] += 1

    for i in nums3:
        for j in nums4:
            if -(i+j) in record:
                count += record[-(i+j)]

    return count
