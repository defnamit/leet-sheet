class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        count=0
        maxm=max(nums)

        for i in range(len(nums)):
            count+=maxm-nums[i]

        return count
