#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = {}
        res = []
        maxfreq = -1
        for key, value in freq.items():
            if value not in bucket:
                bucket[value] = []
            bucket[value].append(key)
            maxfreq = max(maxfreq, value)
        for i in range(maxfreq, -1, -1):
            if len(res) < k and i in bucket:
                res.extend(bucket[i])
        return res[:k]

        
# @lc code=end

#1. hashmap and sort O(NLogN) O(N) space

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = Counter(nums)
    #     freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))
    #     return list(freq.keys())[:k]
#2. hashmap and heap O(NLogN), O(N) space
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # freq = Counter(nums)
    # heap = []
    # res = []
    # for key, value in freq.items():
    #     heapq.heappush(heap, [-value, key])
    # for i in range(k):
    #     res.append(heapq.heappop(heap)[1])
    # return res

#3 hashmap and bucket sort O(N), O(N) space