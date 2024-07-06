import math
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
        
        # return max_profit
        current_min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            # update the current_min if the value of next i is smaller than current_min
            if prices[i] < current_min:
                current_min = prices[i]
            elif prices[i] - current_min > profit:
                profit = prices[i] - current_min
        return profit