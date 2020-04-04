class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        blocks = [[] for _ in range(9)]
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        solved = False

        def placeNext(i, j):
            if i == 8 and j == 8:
                nonlocal solved
                solved = True
                return

            if j == 8:
                backtrack(i + 1, 0)
            else:
                backtrack(i, j + 1)

        def backtrack(i = 0, j = 0):
            if board[i][j] == ".":
                block = i // 3 * 3 + j // 3
                for digit in range(1, 10):
                    if digit not in blocks[block] and digit not in rows[i] and digit not in columns[j]:
                        # place digit
                        board[i][j] = str(digit)
                        blocks[block].append(digit)
                        rows[i].append(digit)
                        columns[j].append(digit)

                        placeNext(i, j)

                        # reset
                        if not solved:
                            board[i][j] = "."
                            blocks[block].remove(digit)
                            rows[i].remove(digit)
                            columns[j].remove(digit)
                        else:
                            return True
            else:
                placeNext(i, j)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    block = i // 3 * 3 + j // 3
                    digit = int(board[i][j])
                    blocks[block].append(digit)
                    rows[i].append(digit)
                    columns[j].append(digit)

        backtrack()




if __name__ == "__main__":
    b = Solution()
    a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    b.solveSudoku(a)
    print(a)