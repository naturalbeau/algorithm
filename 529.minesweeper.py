#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        dx = [0, 0, -1, -1, -1, 1, 1, 1]
        dy = [1, -1, 0, 1, -1, 0, 1, -1]
        x = click[0]
        y = click[1]
        def getNum(x, y):
            num = 0
            for i in range(8):
                newx = x + dx[i]
                newy = y +  dy[i]
                if newx < 0 or newx >= m or \
                    newy < 0 or newy >= n:
                    continue
                if board[newx][newy] in ['M', 'X']:
                    num += 1
            return num

        def dfs(x, y):
            if x < 0 or x>=m or y < 0 or y >= n or board[x][y] != 'E':
                return
            num = getNum(x, y)
            if num == 0:
                board[x][y] = 'B'
                for i in range(8):
                    newx = x + dx[i]
                    newy = y + dy[i]
                    dfs(newx, newy)
            else:
                board[x][y] = str(num)
                
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        dfs(x, y)
        return board

        
            
# @lc code=end

