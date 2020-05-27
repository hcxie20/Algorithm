'''
How to find the biggest rectangle one unit is in?
- find height upward
- then find left 
- and right
'''


class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        height = [0] * n
        left = [0] * n
        right = [n] * n

        max_area = 0

        for i in range(m):
            cur_left = 0
            cur_right = n

            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(cur_left, left[j])
                else:
                    cur_left = j + 1
                    # !! reset to 0, so next row will not consider this left
                    left[j] = 0

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(cur_right, right[j])
                else:
                    cur_right = j
                    right[j] = n
            
            for j in range(n):
                max_area = max(max_area, (right[j] - left[j]) * height[j])
            #     print(i, max_area)
            # print(height)
            # print(left)
            # print(right)
        
        return max_area
