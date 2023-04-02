class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:

        stack = []
        actions = []
        
        for i in range(1,n+1):
            stack.append(i)
            actions.append("Push")

            if i not in (target):
                print("{} not in range".format(i))
                stack.pop()
                actions.append("Pop")

            if stack == target:
                return actions
        
        return actions



s = Solution()
target = [1,2]
n = 4
print(s.buildArray(target,n))