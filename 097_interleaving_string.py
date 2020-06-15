class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1] and dp[0][j - 1] == True:
                dp[0][j] = True
            else:
                break

        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1] and dp[i - 1][0] == True:
                dp[i][0] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])

        return dp[-1][-1]
