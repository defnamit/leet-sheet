class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        minm=min(nums)
        count=0

        for i in range(len(nums)):
            count+=nums[i]-minm

        return count

        #return sum(nums) - len(nums) * min(nums)
