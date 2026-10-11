class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        n=len(nums)

        return sum(nums[i]**2 for i in range(n) if(n%(i+1)==0))

