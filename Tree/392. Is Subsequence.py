class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        left = 0
        right = 0
        while left < len(s) and right < len(t):
            while right < len(t) and s[left] != t[right]:
                right += 1
            if s[left] == t[right]:
                left += 1
                right += 1
        return left == len(s)


if __name__ == '__main__':
    print(Solution().isSubsequence("bb", "ahbgdc"))