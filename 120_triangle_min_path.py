class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return 0

        m = len(triangle)
        n = len(triangle[-1])

        dp = [[float('inf') for _ in range(n)] for _ in range(m)]

        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        return min(dp[-1])
