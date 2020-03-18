class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        rst = []
        
        rows = len(matrix)
        columns = len(matrix[0])

        i, j = 0, 0
        direction = 0
        level = 0

        while len(rst) < rows * columns:
            rst.append(matrix[i][j])
            if direction == 0:
                if j < columns - 1 - level:
                    j += 1
                else:
                    i += 1
                    direction = 1
                continue
            if direction == 1:
                if i < rows - 1 - level:
                    i += 1
                else:
                    j -= 1
                    direction = 2
                continue
            
            if direction == 2:
                if j > level:
                    j -= 1
                else:
                    i -= 1
                    direction = 3
                continue
            
            if direction == 3:
                if i > level + 1:
                    i -= 1
                else:
                    j += 1
                    direction = 0
                    level += 1
                continue

        return rst



