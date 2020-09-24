# dp[i][j] = word1[:i] 变到word2[:j]所需的步数
# 关系：
# 1. dp[i-1][j]: delete a word from word1[:i-1]
# 2. dp[i][j-1]: insert(append) a new word to word1[:i]
# 3. dp[i-1][j-1]: replace word1[i] with word2[j]
# and if word1[i] == word2[j], = dp[i-1][j-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(1 + len(word1))]

        for i in range(1, len(word1) + 1):
            dp[i][0] = i

        for i in range(1, len(word2) + 1):
            dp[0][i] = i

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance("horse", "ros"))
