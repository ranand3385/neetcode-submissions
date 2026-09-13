class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNum = set(nums)
        return len(setNum) != len(nums)