#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        x, y, di = 0, 0, 0
        res = 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for command in commands:
            if command == -2:
                di = (di - 1) % 4
            elif command == -1:
                di = (di + 1) % 4
            else:
                dx , dy= direction[di]
                for k in range(command):
                    if (x + dx, y + dy) not in obstacles:
                        x += dx
                        y += dy
                        res = max(res, x**2 + y**2)
                    else:
                        break
        return res
# @lc code=end

