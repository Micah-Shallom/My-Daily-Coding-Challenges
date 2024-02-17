class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_val = float("inf")
        max_profit = 0
        for i in prices:
            min_val = min(min_val, i)
            profit = i - min_val
            max_profit = max(max_profit,profit)
        return max_profit
    

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))