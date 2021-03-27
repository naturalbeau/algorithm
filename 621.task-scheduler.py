#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        sorted(counts.items(), key=lambda item:item[1])
        maxFre = max(counts.values())
        idle_slots = (maxFre - 1) * (n + 1)
        for i in counts:
            if counts[i] == maxFre:
                idle_slots += 1
            idle_slots -= counts[i]
        return max(len(tasks) + idle_slots , len(tasks))
# @lc code=end

#1 math
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     counts = collections.Counter(tasks)
    #     maxFre = max(counts.values())
    #     extra_length = sum(1 for i in counts if counts[i] == maxFre)
    #     res = (maxFre - 1) * (n + 1) + extra_length
    #     return max(res, len(tasks))