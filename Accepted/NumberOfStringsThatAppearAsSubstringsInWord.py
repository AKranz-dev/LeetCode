class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:

        counter = 0

        for pattern in patterns:
            if pattern in word:
                counter += 1
        return counter


s = Solution()
patterns = ["a","abc","bc","d"]
word = "abc"
print(s.numOfStrings(patterns,word))
