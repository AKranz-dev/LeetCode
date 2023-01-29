class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        listA = []
        for i in range(n):
                listA.append(nums[i])
                listA.append(nums[n+i])
        return listA

