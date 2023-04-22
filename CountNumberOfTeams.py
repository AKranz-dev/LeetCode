class Solution:
    def numTeams(self, rating: list[int]) -> int:

        res = 0
        
        for x in range (len(rating)-2):
            for y in range (1,len(rating)-1):
                for z in range (2,len(rating)):
                    print("{},{},{}".format(rating[x],rating[y],rating[z]))
                    if rating[x] > rating[y] and rating[y] > rating[z]:
                        res +=1
                        print("{},{},{}".format(rating[x],rating[y],rating[z])+"***")
                    elif rating[x] < rating[y] and rating[y] < rating[z] and rating[z] < len(rating):
                        res +=1
        
        
        return res
                        




            

rating = [2,5,3,4,1]
s = Solution()
print(s.numTeams(rating))