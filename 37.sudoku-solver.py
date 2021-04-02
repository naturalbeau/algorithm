#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.is_valid(board, i, j, c):
                            board[i][j] = c
                            if  self.solve(board):
                                return True
                        board[i][j] = '.'
                    return False
        return True

    def is_valid(self, board, x, y, c):
        for i in range(9):
            if board[x][i] == c:
                return False
            if board[i][y] == c:
                return False
        for i in range(3):
            for j in range(3):
                if board[x//3*3+i][y//3*3+j] == c:
                    return False
        return True
# @lc code=end

