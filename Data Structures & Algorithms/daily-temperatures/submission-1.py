class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for t in range(len(temperatures)):
            while stack and (temperatures[t] > temperatures[stack[-1]]):
                currIndex = stack.pop()
                res[currIndex] = t - currIndex
            stack.append(t)
        return res
                    






        