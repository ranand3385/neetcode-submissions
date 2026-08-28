class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            numCount[num] += 1
        
        for num, cnt in numCount.items():
            freq[cnt].append(num)
        output = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output

