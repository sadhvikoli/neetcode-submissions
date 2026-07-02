class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            # Update the lowest price seen so far
            min_price = min(min_price, price)
            # Calculate the profit if we sold at current price
            profit = price - min_price
            # Update max_profit if this transaction is the most profitable
            max_profit = max(max_profit, profit)
            
        return max_profit
