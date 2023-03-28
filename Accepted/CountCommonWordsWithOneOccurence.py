class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:

        counter = 0
        wordDict = {}

        for word in words1:
            if words1.count(word) == 1 and words2.count(word) == 1 and word not in wordDict:
                counter +=1
                wordDict[word] = 1


        for word in words2:
            if words1.count(word) == 1 and words2.count(word) == 1 and word not in wordDict:
                counter +=1
                wordDict[word] = 1

        return counter


words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

s = Solution()
print(s.countWords(words1,words2))