class Solution(object):
    def minimumDeletions(self, nums):

        n=len(nums)
        small_i=nums.index(min(nums))
        big_i=nums.index(max(nums))

        if(small_i > big_i):
            small_i,big_i=big_i,small_i

        case1=(small_i+1) + (n-big_i)
        case2=big_i+1
        case3=n-small_i

        return min(case1,case2,case3)
