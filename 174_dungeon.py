class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 1

        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[-1][-1] = max(- dungeon[-1][-1] + 1, 1)

        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1] + (-dungeon[i][-1]), 1)

        for j in range(n - 2, -1, -1):
            dp[-1][j] = max(dp[-1][j + 1] + (-dungeon[-1][j]), 1)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) + (-dungeon[i][j]), 1)

        return dp[0][0]
