import collections
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    a = collections.Counter(nums1)
    b = collections.Counter(nums2)

    result = []

    less = nums1 if len(nums1) < len(nums2) else nums2

    for c in list(set(less)):
        number = min(a[c], b[c])
        result.extend([c for _ in range(number)])

    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))
