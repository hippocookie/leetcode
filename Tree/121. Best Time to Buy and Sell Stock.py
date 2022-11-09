from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = 100000
        for p in prices:
            min_price = min(p, min_price)
            if p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit

if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))