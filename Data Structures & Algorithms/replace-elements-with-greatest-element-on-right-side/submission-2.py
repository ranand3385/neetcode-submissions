class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = [0] * len(arr)
        currMax = -1

        for i in range(len(arr) - 1, -1, -1):
            right[i] = currMax
            currMax = max(currMax, arr[i])
        
        return right


