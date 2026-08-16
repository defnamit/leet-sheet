class Solution(object):
    def findMissingElements(self, nums):
        miss=[]
        maxx=max(nums)
        minn=min(nums)
        for i in range(minn,maxx+1):
            if(i not in nums):
                miss.append(i)
        
        return miss
        
