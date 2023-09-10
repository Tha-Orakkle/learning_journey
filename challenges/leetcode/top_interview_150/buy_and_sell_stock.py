#!/usr/bin/python3
"""finds the best time to buy and sell stock"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        checked = set()
        profit = 0
        for i in range(len(prices)):
            price = prices[i]
            if price not in checked:
                checked.add(price)
                sell = max(prices[i:])
                diff = sell - price
                if diff > profit:
                    profit = diff
        return profit
