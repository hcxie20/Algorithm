class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        columns = len(grid[0])
        if not rows or not columns:
            return 0
        
        rottens = []
        fresh = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rottens.append([i, j])
                    continue
                if grid[i][j] == 1:
                    fresh += 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        time = 0
        
        while True:
            new_rottens = []
            for rotten in rottens:
                i, j = rotten[0], rotten[1]
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        new_rottens.append([ni, nj])
            if not new_rottens:
                if fresh == 0:
                    return time
                return -1
            time += 1
            rottens = new_rottens

if __name__ == "__main__":
    a = Solution()
    print(a.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))