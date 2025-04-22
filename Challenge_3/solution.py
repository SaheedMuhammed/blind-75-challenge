class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # tow pointer
        left, right = 0, 1
        profit = 0

        while right < len(prices):
        # Check if profitable
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right  # Update left pointer to the current right 

            right += 1  # Move the right pointer forward

        return profit