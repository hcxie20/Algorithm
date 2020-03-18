class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 > -1 and p2 > -1:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # add remains from nums2
        # no need to "add" from nums1
        nums1[:p2+1] = nums2[:p2+1]


Solution().merge([0], 0, [1], 1)