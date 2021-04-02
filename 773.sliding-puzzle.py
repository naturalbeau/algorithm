#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = board[0] + board[1]
        s = ''.join([str(c) for c in s])
        visited = set()
        cnt = 0
        queue = [s]
        directions = {0:[1,3],
                        1:[0,2,4],
                        2:[1,5],
                        3:[0,4],
                        4:[1,3,5],
                        5:[2,4]}
        while queue:
            new = []
            for s in queue:
                if s == '123450':
                    return cnt
                visited.add(s)
                s_list = [int(i) for i in s]
                index = s_list.index(0)
                for direction in directions[index]:
                    news_list = s_list[:]
                    news_list[index],news_list[direction] = news_list[direction],news_list[index]
                    news = ''.join([str(i) for i in news_list])
                    if news not in visited:
                        visited.add(news)
                        new.append(news)
            cnt += 1
            queue = new
        return -1

# @lc code=end

#1 BFS