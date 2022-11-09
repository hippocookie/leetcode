from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        profits = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                profits += profit
        return profits


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))

