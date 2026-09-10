class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        curMin = float('inf')

        for price in prices:
            curMin = min(curMin, price)
            maxPrice = max(maxPrice, price - curMin)
        
        return maxPrice