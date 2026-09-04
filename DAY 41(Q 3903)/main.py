class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        point=0
        last=len(nums)-1

        while(point <= last):
            score=max(nums[:point+1]) - min(nums[point:last+1])

            if(score<=k):
                return point

            point+=1

        return -1
