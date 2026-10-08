class Solution(object):
    def missingInteger(self, nums):
        prefix = nums[0]

        i = 1

        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix += nums[i]
            i += 1

        nums_set = set(nums)

        while prefix in nums_set:
            prefix += 1

        return prefix
