class Solution:
    def exist(self, board, word):
        if len(word) == 0:
            return False

        firstLetter = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    firstLetter.append([i, j])

        def dfs(i, j, num, seen):
            if num == len(word):
                return True

            for direction in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_i, new_j = i + direction[0], j + direction[1]
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and [new_i, new_j] not in seen:
                    if word[num] == board[new_i][new_j]:
                        if dfs(new_i, new_j, num+1, seen + [[new_i, new_j]]):
                            return True

            return False

        for cell in firstLetter:
            if dfs(cell[0], cell[1], 1, [[cell[0], cell[1]]]):
                return True
        return False

# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(Solution().exist([["a","a"]], "aaa"))
