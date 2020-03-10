# for 2 lists with length m, n. 
# Assume m <= n
# splite those lists in to 2 parts, respectively
# let i, j = position to split lists 
# i belongs [0, m]
# j belongs [0, n]
# left1, right1, 
# left2, right2
# j = int((m+n+1)/2) - i
# # if m+n = even, clearly left1+2, right1+2 same length
# # if m+n = odd, left1+2 > right1+2. 1 greater
# 1. consider when i, j != 0, m, n !!!!!!!!!!!!!!!!
# to let 0 < j < n, ######### m <= n
# # m<=n, i > 0, j = int((m+n+1)/2) - i <= int((n+n+1)/2)-i < n - i < n
# # m<=n, i < m, j = int((m+n+1)/2) - i >= int((m+m+1)/2)-i > m - i > 0
# and max(left1+2) <= min(right(1+2))
# -> 
# left1[i-1] <= right2[j]
# left2[j-1] <= right1[i]
# ->
# if nums1[i-1] > nums2[j]: i decrease
# else(nums2[j-1]>nums1[i]): i increase
# decrease, increase in binary search
# 2. when i or j = 0, m, n
# if i == 0: 
# max(left1+2) = nums2[j-1] < nums1[i]
# if j == 0:
# max(left1+2) = nums1[i-1] < nums2[j]
# if i == m:
# min(right1+2) = nums2[j] > nums1[i]
# if j == n:
# min(right1+2) = nums1[i] >nums2[j]



class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2
        m = len(A)
        n = len(B)

        odd = (m+n)%2

        iMin = 0
        iMax = m

        maxLeft = 0
        minRight = 0
        

        while iMin <= iMax:
            i = int((iMin + iMax)/2)
            j = int((m+n+1)/2) - i
            
            if i > iMin and B[j-1] > A[i]:
                # i increaes
                iMin = i + 1
            elif i < iMax and j != n and A[i-1] > B[j]:
                # i decrease
                iMax = i - 1
            else:
                # found
                if i == 0:
                    maxLeft = B[j-1]
                elif j == 0:
                    maxLeft = A[i-1]
                else:
                    maxLeft = max(A[i-1], B[j-1])  
                if odd:
                    return maxLeft

                if i == m:
                    minRight = B[j]
                elif j == n:
                    minRight = A[i]
                else:
                    minRight = min(B[j], A[i])
                return (maxLeft + minRight)/2


print(Solution().findMedianSortedArrays([1, 3], [2]))