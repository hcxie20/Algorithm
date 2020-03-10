# [4, 5, 6, 7, 0, 1, 2, 3]
# nums[mid] 与target 是否在同一侧（递增数列）
# 是则用target比
# 否则用inf, -inf比
# [4, 5, 6, 7, 0, 1, 2, 3], mid = 3, 
# target = 5, 同一侧, num = 7
# target = 0, 不同侧，num = -inf

class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            else:
                if target < nums[0]:
                    num = float("-inf")
                else:
                    num = float("inf")
            
            if num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
            else:
                return mid
        
        return -1