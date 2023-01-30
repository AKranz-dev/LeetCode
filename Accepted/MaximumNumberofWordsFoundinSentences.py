class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        import re
        resultList = []
        pattern = r"[A-Za-z0-9]+"
        for sentence in sentences:
            result = re.findall(pattern,sentence)
            resultList.append(len(result))
        return max(resultList)


s = Solution()
sentences = ["w jrpihe zsyqn l dxchifbxlasaehj","nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom","xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg","krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm","rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr","o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk","hrvh efqvjilibdqxjlpmanmogiossjyxepotezo","qstd zui nbbohtuk","qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"]

print(s.mostWordsFound(sentences))







#Would it be faster to import re and look for words using regex? Or simply to parse throuh the sentences and look for spaces?