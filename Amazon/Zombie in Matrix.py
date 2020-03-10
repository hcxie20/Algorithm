def solution(grid):
    time = 0
    rows = len(grid)
    columns = len(grid[0])
    if not rows or not columns:
        return 0

    zoombies = [[i, j] for i in range(rows) for j in range(columns) if grid[i][j] == 1]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while True:
        new_zoombies = []
        for zoombie in zoombies:
            i, j = zoombie[0], zoombie[1]
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][j] == 0:
                    grid[ni][nj] = 1
                    new_zoombies.append([ni, nj])
        if not new_zoombies:
            return time
        time += 1
        zoombies = new_zoombies
    pass




if __name__ == "__main__":
    grid = [[0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]]
    
    print(solution(grid))