class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        left = (len(nums1) + len(nums2)) // 2
        right = left + 1

        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.find_K_smallest(nums1, nums2, right)

        else:
            return 0.5 * (self.find_K_smallest(nums1, nums2, left) + self.find_K_smallest(nums1, nums2, right))

    def find_K_smallest(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]

        if not nums2:
            return nums1[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        anchor = k // 2 - 1

        anchor1 = min(len(nums1) - 1, anchor)
        anchor2 = min(len(nums2) - 1, anchor)

        if nums1[anchor1] < nums2[anchor2]:
            nums1, nums2 = nums2, nums1
            anchor1, anchor2 = anchor2, anchor1

        return self.find_K_smallest(nums1, nums2[anchor2 + 1:], k - anchor2 - 1)


if __name__ == '__main__':
    ls2 = [1]
    ls1 = [2, 3, 4, 5, 6]
    print(Solution().findMedianSortedArrays(ls1, ls2))
