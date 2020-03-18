# class Solution:
#     def singleNumber(self, nums) -> int:
#         return 2 * sum(set(nums)) - sum(nums)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

Solution().singleNumber([1, 1, 2, 2, 3, 4, 4])

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。