class Solution:
    def longestPalindrome(self, s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # dp[i][j] s[i][j]
        rst = [0, 0, 0]
        #0: length 1: start 2: end

        # set length = 1 to true
        for i in range(len(s)):
            dp[i][i] = True

        # set length = 2, baseline
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                if 2 > rst[0] and dp[i][i+1]:
                    rst = [2, i, i+1]

        # start iteration
        # dp[i][j] = True if dp[i+1][j-1] == True
        for length in range(2, len(s)):
            for i in range(len(s) - length):
                if s[i] == s[i+length]:
                    dp[i][i+length] = dp[i+1][i+length-1]
                    if length + 1 > rst[0] and dp[i][i+length]:
                        rst = [length+1, i, i+length]
        return s[rst[1]:rst[2]+1]

print(Solution().longestPalindrome("aab"))