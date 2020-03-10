class Solution:
    def maxSubArray(self, nums):
        l = len(nums)
        dp = [0 for i in range(l)]
        mx = float("-inf")
        
        for ln in range(1, l):
            for i in range(l-ln+1):
                dp[i] = dp[i] + nums[i+ln-1]
                if dp[i] > mx:
                    mx = dp[i]
        
        return mx
a = Solution()
a.maxSubArray([1])

