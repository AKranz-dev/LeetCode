class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0
        if ruleKey == "type":
            targetIndex = 0
        elif ruleKey == "color":
            targetIndex = 1
        elif ruleKey == "name":
            targetIndex = 2
        
        for item in items:
            if item[targetIndex] == ruleValue:
                counter+=1
        return counter
        




s = Solution()
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(s.countMatches(items,ruleKey,ruleValue))