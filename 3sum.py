class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rst = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) - 1
                while low < high:
                    tmp = nums[i] + nums[low] + nums[high]
                    if tmp == 0:
                        rst.append([nums[i], nums[low], nums[high]])
                        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -=1
                        low += 1
                        high -= 1
                    elif tmp < 0:
                        low += 1
                    else:
                        high -= 1
        return rst