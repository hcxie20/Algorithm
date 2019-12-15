class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
    def solve(self, board):
        num = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in range(1, 10):
                        if self.isValid(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True
    
    def isValid(self, board, r, c, num):
        for i in range(9):
            if board[r][i] == num:
                return False
            
        for i in range(9):
            if board[i][c] == num:
                return False
            
        for i in range(r-r%3, r-r%3+3):
            for j in range(c-c%3, c-c%3+3):
                if board[i][j] == num:
                    return False
        
        return True
        
if __name__ == "__main__":
    b = Solution()
    a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    b.solveSudoku(a)
    print(a)