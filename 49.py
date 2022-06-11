from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    record = defaultdict(list)

    for str in strs:
        key = "".join(sorted(str))
        record[key].append(str)
    return list(record.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
