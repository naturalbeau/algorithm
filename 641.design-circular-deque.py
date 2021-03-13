#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class DoubleLinkedListNode:
    def __init__(self, value, prev=None, next=None):
        self.val = value
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.count = 0
        self.k = k
        self.head = DoubleLinkedListNode(0)
        self.tail = DoubleLinkedListNode(0)
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head

        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        newNode = DoubleLinkedListNode(value)
        tempNode = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = tempNode
        tempNode.prev = newNode
        self.count += 1
        return True

        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        newNode = DoubleLinkedListNode(value)
        tempNode = self.tail.prev
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = tempNode
        tempNode.next = newNode
        self.count += 1
        return True
        
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.count -= 1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        tempNode = self.tail.prev
        self.tail.prev = tempNode.prev
        self.tail.prev.next = self.tail
        self.count -= 1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.head.next.val
        
    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.tail.prev.val

        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.k
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

#array
#double linked list


# class MyCircularDeque:

#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the deque to be k.
#         """
#         self.deque = [0] * k
#         self.headindex = 0
#         self.count = 0
#         self.k = k

#     def insertFront(self, value: int) -> bool:
#         """
#         Adds an item at the front of Deque. Return true if the operation is successful.
#         """
#         if self.isFull():
#             return False
#         self.headindex = (self.headindex - 1) % self.k
#         self.deque[self.headindex] = value
#         self.count += 1
#         return True

#     def insertLast(self, value: int) -> bool:
#         """
#         Adds an item at the rear of Deque. Return true if the operation is successful.
#         """
#         if self.isFull():
#             return False
#         self.deque[(self.headindex + self.count) % self.k] = value
#         self.count += 1
#         return True
        

#     def deleteFront(self) -> bool:
#         """
#         Deletes an item from the front of Deque. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False
#         self.headindex = (self.headindex + 1) % self.k
#         self.count -= 1
#         return True
        

#     def deleteLast(self) -> bool:
#         """
#         Deletes an item from the rear of Deque. Return true if the operation is successful.
#         """
#         if self.isEmpty():
#             return False
#         self.count -= 1
#         return True
        

#     def getFront(self) -> int:
#         """
#         Get the front item from the deque.
#         """
#         if self.isEmpty():
#             return -1
#         return self.deque[self.headindex]
        

#     def getRear(self) -> int:
#         """
#         Get the last item from the deque.
#         """
#         if self.isEmpty():
#             return -1
#         return self.deque[(self.headindex + self.count - 1) %  self.k]

        

#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular deque is empty or not.
#         """
#         return self.count == 0

#     def isFull(self) -> bool:
#         """
#         Checks whether the circular deque is full or not.
#         """
#         return self.count == self.k
