from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = float("inf")
        profit = 0

        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)

        return profit
