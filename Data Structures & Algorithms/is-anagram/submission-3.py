class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount, tCount = {}, {}

        for c in s:
            if c not in sCount:
                sCount[c] = 0
            else:
                sCount[c] += 1
        for c in t:
            if c not in tCount:
                tCount[c] = 0
            else:
                tCount[c] += 1
        
        return tCount == sCount