class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        curMin = prices[0]
        for price in prices:
            curMin = min(curMin, price)
            res = max(price - curMin, res)
        return res 