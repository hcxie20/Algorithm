class Solution:
    def PredictTheWinner(self, nums) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]

        for i, num in enumerate(nums):
            dp[i][i] = num

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][length - 1] >= 0


if __name__ == '__main__':
    print(Solution().PredictTheWinner([1, 5, 2]))