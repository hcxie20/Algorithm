class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in seen:
                return [seen[sub], i]
            seen[nums[i]] = i