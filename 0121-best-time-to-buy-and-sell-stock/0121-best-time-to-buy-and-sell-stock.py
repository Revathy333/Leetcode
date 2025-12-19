class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_p = 0

        for price in prices[1:]:
            max_p = max(max_p, price - min_price)
            min_price = min(min_price, price)

        return max_p        



       