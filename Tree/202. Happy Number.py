import unittest

class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(1000000):
            result = 0
            while n > 0:
                digit = n % 10
                result += digit * digit
                n = n // 10
            if result == 1:
                return True
            n = result
        return False

    def isHappy2(self, n:int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            n = get_next(n)
        return n == 1

    def isHappy3(self, n:int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        fast_cursor = get_next(n)
        slow_cursor = n
        while fast_cursor != 1 and slow_cursor != fast_cursor:
            slow_cursor = get_next(slow_cursor)
            fast_cursor = get_next(get_next(fast_cursor))
        return fast_cursor == 1




# class SolutionTest(unittest.TestCase):
#
#     def test(self):
#         self.assertEqual(1, 1)
#

if __name__ == '__main__':
    # unittest.main()
    print(Solution().isHappy3(3))