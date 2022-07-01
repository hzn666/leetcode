from typing import List


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    profit = 0
    cost = prices[0]

    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - cost)
        cost = min(cost, prices[i])

    return profit