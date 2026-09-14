class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        count = 0
        for num in nums:
            if num != 1:
                ones = max(count, ones)
                count = 0
            else:
                count += 1
        
        return max(ones, count)