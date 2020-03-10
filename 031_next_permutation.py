# [1, 3, 4, 2]
# from right to left, find first i s.t. nums[i-1] < nums[i]
# at this time, [i:] is DECENDING!!
# swap nums[i-1] with smallest value which is greater than nums[i-1]
# not [i:] still DECENDING!!
# reverse [i:]

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        re = nums[i:]
                        re.reverse()
                        nums[i:] = re
                        return
        nums.reverse()
        return