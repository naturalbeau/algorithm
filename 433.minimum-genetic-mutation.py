#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        set1 = set([start])
        set2 = set([end])
        step = 0
        while len(set1) > 0 and len(set2) > 0:
            if len(set1) > len(set2):
                set1, set2 = set2, set1
            newset = set()
            for gene in set1:
                newgenes = [gene[:i] + c + gene[i+1:] for c in 'ACGT' for i in range(8)]
                for newgene in newgenes:
                    if newgene in set2:
                        return step + 1
                    if newgene in bank:
                        bank.remove(newgene)
                        newset.add(newgene)
            set1 = newset
            step += 1
        return -1
# @lc code=end
# 1.BFS
    # def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    #     bank = set(bank)
    #     if end not in bank:
    #         return -1
    #     queue = [(start, 0)]
    #     while queue:
    #         gene, level = queue.pop(0)
    #         if gene == end:
    #             return level
    #         newgenes = [gene[:i] + c + gene[i+1:] for c in ['A','C','G','T'] for i in range(8)]
    #         for newgene in newgenes:
    #             if newgene == end:
    #                 return level + 1
    #             if newgene in bank:
    #                 bank.remove(newgene)
    #                 queue.append((newgene, level+1))
    #     return -1
#2. bidirectional BFS