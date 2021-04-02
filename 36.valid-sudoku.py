#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(sx, sy, ex, ey):
            res = []
            for i in range(sx, ex + 1):
                for j in range(sy, ey + 1):
                    if board[i][j] != '.':
                        res.append(board[i][j])
            return len(set(res)) == len(res)
        for i in range(9):
            if not is_valid(i, 0, i, 8):
                return False
            if not is_valid(0, i, 8, i):
                return False
        for i in range(3):
            for j in range(3):
                if not is_valid(i*3, j*3, (i+1)*3-1,(j+1)*3-1):
                    return False
        return True


# @lc code=end

