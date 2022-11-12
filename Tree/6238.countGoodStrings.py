class Solution:


    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.counter = 0
        if low == 0 and high == 0:
            return 0
        self.zeros = ''.join(['0' for i in range(zero)])
        self.ones = ''.join(['1' for i in range(one)])
        s = ""
        self.dfs(s, low, high, zero, one)
        return self.counter % 1000000007

    def dfs(self, s:str, low: int, high: int, zero: int, one: int):
        length = len(s)
        if length > high:
            return
        if low <= length <= high:
            self.counter += 1
            # print(s)

        for i in (0, 1):
            s = self.operate(s, i, zero, one)
            print(s)
            self.dfs(s, low, high, zero, one)
            s = self.reverse(s, i, zero, one)

    def operate(self, s, num, zero, one):
        char = self.zeros if num == 0 else self.ones
        s += char
        return s

    def reverse(self, s, num, zero, one):
        times = zero if num == 0 else one
        return s[0:len(s) - times]

if __name__ == '__main__':
    # print(Solution().countGoodStrings(3, 3, 1, 1))
    print(Solution().countGoodStrings(200, 200, 10, 1))
