class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        slow = fast = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow