class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:

        counter = 0
        kill = 0

        for word in words:
            for i in range (0,len(word)):
                try:
                    if word[i] != s[i]:
                        kill = 1
                except:
                    kill = 1
            if kill !=1:
                counter+=1
            kill= 0
        
        return(counter)
        
        


a = Solution()
words = ["e","s","mi","e","ia","ibwu","e","e","k","ci","rip","suw","a","l"]
s = "e"
print(a.countPrefixes(words,s))
