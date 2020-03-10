# dp
# dp[i] = max sum of sublist ending with nums[i]
# dp[0] = nums[1]
# dp[i] = nums[i] if dp[i-1] < 0
# else dp[i] += nums[i]
# since dp[i] only depends on dp[i-1], i.e., one argument
# dp[] is not needed. One number is enough
class Solution1:
    def maxSubArray(self, nums):
        dp = [None for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

# divide and conquer
# left, mid, right
# 1. result in left
# 2. result cross over mid
# 3. result in right
# divide till 2 numbers in the list, max subarray is the max number
# find the maxmum of these 3 cases, then the result








