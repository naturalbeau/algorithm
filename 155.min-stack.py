#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            del self.min_stack[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

# one stack method O(n) O(n)
#two stack method O(n) O(n)

# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
        

#     def push(self, x: int) -> None:
#         if not self.stack:
#             self.stack.append([x, x])
#         else:
#             self.stack.append([x, min(x, self.stack[-1][1])])

#     def pop(self) -> None:
#         del self.stack[-1]

#     def top(self) -> int:
#         return self.stack[-1][0]
        

#     def getMin(self) -> int:
#         return self.stack[-1][1]