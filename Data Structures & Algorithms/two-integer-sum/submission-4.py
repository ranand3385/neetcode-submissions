class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i in range(len(nums)):
            if target - nums[i] not in pair:
                pair[nums[i]] = i
            else:
                return [pair[target-nums[i]], i]