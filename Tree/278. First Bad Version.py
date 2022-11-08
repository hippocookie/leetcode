def isBadVersion(version: int) -> bool:
    return version >= 2

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right - 1:
            mid = int(left + (right - left) / 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return left if isBadVersion(left) else right

if __name__ == '__main__':
    print(Solution().firstBadVersion(3))