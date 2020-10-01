class Solution:
    def numTrees(self, n, ls):
        if not ls:
            return 0

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1] - dp[len(ls) - len(set(ls))]


if __name__ == '__main__':
    # print(Solution().numTrees(2))
    # print(Solution().numTrees(3))
    print(Solution().numTrees(3, [1, 2, 1]))
    print(Solution().numTrees(2, [1, 1]))
    print(Solution().numTrees(3, [1, 1, 1]))
