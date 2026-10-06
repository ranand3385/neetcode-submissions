class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sp, fp = 0, 1
        maxProfit = 0

        while fp < len(prices):
            if prices[sp] < prices[fp]:
                maxProfit = max(maxProfit, prices[fp] - prices[sp])
            else:
                sp = fp
            fp += 1
        return maxProfit