class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers) + 1
        before_close = [0 for i in range(n)]
        after_close = [0 for i in range(n)]
        for i in range(1, n):
            cost = 1 if customers[i - 1] == 'N' else 0
            before_close[i] = before_close[i - 1] + cost

        for i in range(n - 2, -1, -1):
            cost = 1 if customers[i] == 'Y' else 0
            after_close[i] = after_close[i + 1] + cost

        min_close = 0
        min_cost = n
        for i in range(0, n):
            cost = before_close[i] + after_close[i]
            if cost < min_cost:
                min_cost = cost
                min_close = i
        return min_close





if __name__ == '__main__':
    print(Solution().bestClosingTime('YYNY'))