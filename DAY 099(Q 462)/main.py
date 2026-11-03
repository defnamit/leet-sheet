class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        nums.sort()
        n=len(nums)
        median=nums[n//2]
        count=0

        for i in range(n):
            count+=abs(nums[i]-median)

        return count
