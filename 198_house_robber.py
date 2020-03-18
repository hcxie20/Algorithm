class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        dp = [None for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[0]
                continue
            if i == 1:
                dp[i] = max(nums[0], nums[1])
                continue

            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]