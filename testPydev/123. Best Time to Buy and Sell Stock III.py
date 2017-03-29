class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        prices_len = len(prices)
        stack = [0] * prices_len
        min_val = prices[0]
        for i in range(1, prices_len):
            min_val = min(prices[i], min_val)
            stack[i] = prices[i] - min_val
        print stack

        max_val = prices[prices_len-1]
        max_gap = 0
        max_profit = 0
        for i in range(prices_len-2, -1, -1):
            max_val = max(prices[i], max_val)
            max_gap = max(max_val - prices[i], max_gap)
            max_profit = max(max_gap + stack[i], max_profit)
        print max_profit

if __name__ == "__main__":
    s = Solution()
    s.maxProfit([10,1,9,2,8,3,7,4,6,5,10])