class Solution:
    def longestValidParentheses(self, s):
        dp = [0 for _ in range(len(s)+1)]
        strs = " " + s

        for i in range(1, len(s)+1):
            if strs[i] == ")":
                if strs[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                else:
                    # if increase, there need to be a "(" before the previous longest pair
                    if strs[i - dp[i-1] - 1] == "(":
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)