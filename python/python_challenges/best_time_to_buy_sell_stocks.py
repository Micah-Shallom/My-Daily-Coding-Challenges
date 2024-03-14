class Solution:
    def maxProfit(self, arr: list[int]) -> int:
        max_profit = 0
        localMin = float('inf')
        for currentPrice in arr:
            if currentPrice < localMin:
                localMin = currentPrice
            else:
                max_profit = max(max_profit, currentPrice - localMin)

        return max_profit
    
    def recMaxProfit(self, arr:list[int]) -> int:
        
        def recurse(prices: list[int], minPrice: int, maxProfit: int) -> int:
            if not prices:
                return maxProfit
            current_price = prices[0]
            if current_price < minPrice:
                minPrice =  current_price
            else:
                maxProfit = max(maxProfit, current_price - minPrice)
            return recurse(arr[1:], minPrice, maxProfit)
        
        return recurse(arr, float("inf"), 0)
            


    
print(Solution().maxProfit([7,1,4,5,19,4]))
print(Solution().recMaxProfit([7,1,4,5,19,4]))