class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        countList = []
        for account in accounts:
            runningCount = 0
            for num in account:
                runningCount += num
            countList.append(runningCount)

        countList.sort(reverse=True)
        return countList[0]
