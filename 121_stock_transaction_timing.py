class Solution:
    def maxProfit(self, prices):
        ls = [None] * (len(prices) - 1)
        dp = 0
        rst = 0
        for i in range(len(prices)-1):
            ls[i] = prices[i + 1] - prices[i]
            if i == 0:
                dp = ls[i]
                rst = ls[i]
            else:
                if dp < 0:
                    dp = ls[i]
                else:
                    dp += ls[i]
                if dp > rst:
                    rst = dp
        if rst > 0:
            return rst
        else:
            return 0