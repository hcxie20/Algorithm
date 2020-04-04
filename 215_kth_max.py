# quick select

class Solution:
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, l, r, target):
        pivot = nums[r]
        # or randomly chose between [l, r], and swap with nums[r]
        i = j = l
        while j < r:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[r] = nums[r], nums[i]
        if i > target:
            return self.quickSelect(nums, l, i - 1, target)
        elif i < target:
            return self.quickSelect(nums, i + 1, r, target)
        else:
            return nums[i]