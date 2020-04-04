
# class Solution(object):
#     def __init__(self, grid):
        
#         def find(nodes, level):
#             newNodes = []
#             end = False
#             for node in nodes:
#                 if grid[node[0]][node[1]] == 0:
#                     return level
                
#                 # add next level
#                 for direction in [[0, 1], [1, 0], [1, 1]]:
#                     i, j = node[0] + direction[0], node[1] + direction[1]
#                     if 0 <= i < row and 0 <= j < column:
#                         if [i, j] not in nodes and [i, j] not in newNodes:
#                             newNodes.append([i, j])
#                     else:
#                         end = True
                            
#             if not newNodes or end:
#                 return level + 1
#             return find(newNodes, level + 1)

#         if not grid:
#             print(0)
            
#         rst = 0
#         #print(grid)
#         row = len(grid)
#         column = len(grid[0])
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 rst = max(rst, find([[i, j]], 0))
#         print(rst ** 2)


# grid = [
#     [1,0,1,0,1,1,1,1,1,1],
#     [0,0,0,0,0,0,0,1,1,1],
#     [1,0,1,0,1,1,0,1,1,1],
#     [0,0,0,0,1,1,1,1,1,1],
#     [1,0,1,0,1,1,1,1,1,1],
#     [0,0,0,0,0,0,1,1,1,1],
#     [1,0,1,0,1,1,1,1,1,1],
#     [0,0,0,0,1,1,0,0,0,1]
# ]
# length = 3
# Solution(grid)




class Solution(object):
    def fight(self, grid):
        
        def findPath(node, target, threshold, been, num):
            if node == target:
                return num
            rst= float("inf")
            for direction in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                i, j = node[0] + direction[0], node[1] + direction[1]
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] <= threshold and [i, j] not in been:
                    rst = min(findPath([i, j], target, threshold, been + [[i, j]], num + 1), rst)
            return rst


        if not grid:
            print(0)
            return
        aims = [[1, 0, 0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and grid[i][j] != 1:
                    aims.append([grid[i][j], i, j])
        aims.sort()
        rst = 0
        for i in range(1, len(aims)):
            rst += findPath([aims[i-1][1], aims[i-1][2]], [aims[i][1], aims[i][2]], aims[i][0], [], 0)
        print(rst)
        pass

grid = [
    [1, 2, 3, 7],
    [0, 0, 4, 8],
    [0, 6, 5, 9]
]
Solution().fight(grid)