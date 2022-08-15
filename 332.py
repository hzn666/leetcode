from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dict = defaultdict(list)
        for depart, arrive in tickets:
            tickets_dict[depart].append(arrive)

        res = []

        def backtracking(depart, path):
            if len(path) == len(tickets) + 1:
                res.extend(path)
                return True

            tickets_dict[depart].sort()
            
            for _ in tickets_dict[depart]:
                arrive = tickets_dict[depart].pop(0)
                if backtracking(arrive, path+[arrive]):
                    return True
                tickets_dict[depart].append(arrive)

        backtracking('JFK', ['JFK'])
        return res
