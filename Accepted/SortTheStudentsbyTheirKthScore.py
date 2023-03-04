class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:

        dict = {}
        sortList = []
        returnList = []

        #Dictionary where the key is the exam grade we care about, and the value is the student! (AKA the index of the score list)
        for i in range (0,len(score)):
            student = score[i]
            targetGrade = student[k]

            dict[targetGrade] = i

        for entry in dict:
            sortList.append(entry)
        
        sortList.sort(reverse=True)

        for item in sortList:
            student = dict[item]
            returnList.append(score[student])
        
        return returnList

        


            







s = Solution()
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2

print(s.sortTheStudents(score,k))