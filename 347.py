import collections
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    result = collections.Counter(nums)
    result = dict(sorted(result.items(), key=lambda x: x[1]))
    return list(result.keys())[::-1][:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
topKFrequent(nums, k)
