from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(p) > len(s):
            return []
        indexes = []
        s_len = len(s)
        p_len = len(p)
        for i in range(s_len):
            for j in range(i, i + p_len):
                

        return indexes

