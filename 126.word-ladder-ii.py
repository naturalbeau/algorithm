#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    return layer[w]
                newWords = [w[:i] + c + w[i+1:] for c in string.ascii_lowercase 
                            for i in range(len(beginWord))]
                for newWord in newWords:
                    if newWord in wordList:
                        newlayer[newWord] += [j + [newWord] for j in layer[w]]
            layer = newlayer
            wordList -= set(newlayer.keys())
        return newlayer
# @lc code=end

# BFS with hashmap