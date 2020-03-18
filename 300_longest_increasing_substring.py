class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            dpMax = 0
            for j in range(i):
                if nums[j] < nums[i] and dpMax < dp[j]:
                    dpMax = dp[j]
            dp[i] = dpMax + 1
        return max(dp)