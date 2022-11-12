from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        length = len(cost)
        total_cost: List[int] = [0 for i in range(length + 1)]
        for i in range(2, length + 1):
            total_cost[i] = min(total_cost[i - 1] + cost[i - 1], total_cost[i - 2] + cost[i - 2])
        return total_cost[len(cost)]

if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([10, 15, 20]))
    print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))





