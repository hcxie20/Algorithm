class Solution:
    def canJump(self, nums) -> bool:
        if not nums:
            return True
        if len(nums) == 1:
            return True

        i = len(nums) - 1
        while i > -1:
            if nums[i] == 0 and i != len(nums) - 1:
                j = i - 1
                while j > -1:
                    if nums[j] > i - j:
                        i = j - 1
                        break
                    j -= 1
                if i != j - 1:
                    return False
            else:
                i -= 1
        return True
