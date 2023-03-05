class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        alt = 0
        altTrack = 0

        for i in range(0,len(gain)):
            altTrack += gain[i]

            if altTrack > alt:
                alt = altTrack
        return alt



s = Solution()
gain = [-4,-3,-2,-1,4,3,2]
print(s.largestAltitude(gain))