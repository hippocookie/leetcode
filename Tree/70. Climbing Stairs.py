class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        steps = [0 for i in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2, n):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n - 1]

if __name__ == '__main__':
    print(Solution().climbStairs(3))


