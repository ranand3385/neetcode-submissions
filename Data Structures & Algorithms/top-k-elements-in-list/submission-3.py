class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)

        for num in nums:
            numCount[num] += 1
        output = []    
        while len(output) < k:
            num = max(numCount, key=numCount.get)
            numCount.pop(num)
            output.append(num)

        return output
