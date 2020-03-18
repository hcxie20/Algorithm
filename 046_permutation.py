class Solution:
    def permute(self, nums):
        self.rst = []
        def permutation(remains, ans):
            if not remains:
                self.rst.append(ans)

            for i in range(len(remains)):
                permutation(remains[:i] + remains[i+1:], ans + [remains[i]])

        permutation(nums, [])
        return self.rst