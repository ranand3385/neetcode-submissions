class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = []
        for i in range(0, len(arr)):
            if i == len(arr) - 1:
                right.append(-1)
            else:
                right.append(max(arr[i + 1:len(arr)]))
        return right
