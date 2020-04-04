class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        l = 0
        r = len(nums) - 1
        p = 0
        while p <= r:
            if nums[p] == 0:
                nums[p], nums[l] = nums[l], nums[p]
                p += 1
                l += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
        return nums
        