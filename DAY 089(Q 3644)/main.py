class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        c = -1

        for i in range(len(nums)):
            if i != nums[i]:
                c &= nums[i]

        return max(c, 0)
