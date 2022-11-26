class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n < 1:
            return 1
        binary = bin(n)
        if binary.count("1") == 1:
            result = 0
            while n > 1:
                n = n >> 1
                result += 1
            return result
        else:
            return n



if __name__ == '__main__':
    print(Solution().numberOfCuts(3))
    print(Solution().numberOfCuts(4))
    print(Solution().numberOfCuts(5))
    print(Solution().numberOfCuts(6))
    print(Solution().numberOfCuts(7))
    print(Solution().numberOfCuts(8))
