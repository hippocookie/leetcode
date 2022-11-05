class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s_to_t = {}
        dic_t_to_s = {}
        for i, c in enumerate(s):
            tc = t[i]
            if tc in dic_t_to_s and dic_t_to_s[tc] is not c:
                return False
            if c in dic_s_to_t and dic_s_to_t[c] is not tc:
                return False
            dic_s_to_t[c] = tc
            dic_t_to_s[tc] = c
            zip()
        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic("paper", "title"))