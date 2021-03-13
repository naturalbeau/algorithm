#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.count = 0
        self.headindex = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[(self.headindex + self.count) % self.k] = value
        self. count += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.headindex = (self.headindex + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.headindex]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.headindex + self.count - 1 ) % self.k]


    def isEmpty(self) -> bool:
        return self.count  == 0

    def isFull(self) -> bool:
        return self.count  == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

