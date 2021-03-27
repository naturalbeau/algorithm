#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        set1 = set([beginWord])
        set2 = set([endWord])
        wordList.remove(endWord)
        step = 1
        while len(set1) > 0 and len(set2) > 0:
            newset = set()
            if len(set1) > len(set2):
                set1, set2 = set2, set1
            for word in set1:
                newWords = [word[:i] + c + word[i+1:] for i in range(len(word)) 
                            for c in string.ascii_lowercase]
                for newWord in newWords:
                    if newWord in set2:
                        return step + 1
                    if newWord not in wordList:
                        continue
                    wordList.remove(newWord)
                    newset.add(newWord)
            
            set1 = newset
            step += 1
            
        return 0

# @lc code=end

#1 BFS 
# Time Complexity O(n^2*26*wordLength)
# Space Complexity O(n)

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     wordList = set(wordList)
    #     queue = [(beginWord, 1)]
    #     while queue:
    #         word, level = queue.pop(0)
    #         if word == endWord:
    #             return level
    #         for i in range(len(beginWord)):
    #             for c in string.ascii_lowercase:
    #                 newWord = word[:i]+c+word[i+1:]
    #                 if newWord in wordList:
    #                     queue.append((newWord, level+1))
    #                     wordList.remove(newWord)
    #     return 0
# 2 Bidirectional BFS
# O(wordlength*26*n^2)