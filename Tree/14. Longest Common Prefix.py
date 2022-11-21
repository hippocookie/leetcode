from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        index = 0
        result = ""
        while True:
            char = ""
            for s in strs:
                if index == len(s) or (char != "" and char != s[index]):
                    return result
                char = s[index]
            result += char
            index += 1


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))
