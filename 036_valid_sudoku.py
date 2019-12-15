class Solution:
    def isValidSudoku(self, board):
        memo = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    tmp = "(" + board[i][j] + ")"
                    if (str(i)+tmp) in memo or (tmp+str(j)) in memo or (str(int(i/3))+ tmp+str(int(j/3))) in memo:
                        return False
                    else:
                        memo.add(str(i) + tmp)
                        memo.add(tmp + str(j))
                        memo.add(str(int(i/3))+ tmp+str(int(j/3)))
        return True


if __name__ == "__main__":
    a = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    b = Solution()
    print(b.isValidSudoku(a))
