class Solution(object):
    def missingMultiple(self, nums, k):
        
        s = set(nums)

        i = 1m

        while True:
            multiple = k * i

            if multiple not in s:
                return multiple

            i += 1
