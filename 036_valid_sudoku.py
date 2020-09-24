class Solution:
    def isValidSudoku(self, board) -> bool:
        blocks = [[] for _ in range(9)]
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    block = i // 3 * 3 + j // 3
                    num = int(board[i][j])
                    if num not in blocks[block] and num not in rows[i] and num not in columns[j]:
                        blocks[block].append(num)
                        rows[i].append(num)
                        columns[j].append(num)
                    else:
                        return False

        return True


if __name__ == "__main__":
    a = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    b = Solution()
    print(b.isValidSudoku(a))
