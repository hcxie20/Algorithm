class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid:
            return 0
        
        self.grid = grid
        mx = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    mx = max(mx, self.dfs(i, j, 0))
        return mx

    def dfs(self, i, j, num):
        for direction in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            new_i, new_j = i + direction[0], j + direction[1]
            if 0 <= new_i < len(self.grid) and 0 <= new_j < len(self.grid[0]):
                if self.grid[new_i][new_j] == 1:
                    self.grid[new_i][new_j] = 0
                    num = self.dfs(new_i, new_j, num)

        return num + 1

# print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(Solution().maxAreaOfIsland([[1, 1]]))

