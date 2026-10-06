class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        l, res = 0, 0

        for r in range(len(s)):
            if s[r] in indexMap:
                l = max(indexMap[s[r]] + 1, l)
            indexMap[s[r]] = r
            res = max(res, r - l + 1)
                

        return res

