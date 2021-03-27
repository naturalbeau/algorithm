#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = float('-inf')
        for left in range(n):
            prefixSum = [0] *  m
            for right in range(left, n):
                for i in range(m):
                    prefixSum[i] += matrix[i][right]
                res = max(res, self.helper(prefixSum, k))
        return res
    def helper(self, prefixSum, k):
        res = float('-inf')
        m = len(prefixSum)
        cur = 0
        subMatrixSum = [0]
        for i in range(m):
            cur += prefixSum[i]
            idx = bisect.bisect_left(subMatrixSum, cur - k)
            if idx >=0 and idx < len(subMatrixSum):
                res = max(res, cur - subMatrixSum[idx])
            bisect.insort(subMatrixSum, cur)
        return res

# @lc code=end

# O(N^2 M logM)