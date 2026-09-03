class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Step 1: Find the minimum element in the array
        min_val = min(nums1)
        
        # Step 2: If the minimum value is odd, it's always possible
        if min_val % 2 != 0:
            return True
            
        # Step 3: If the minimum value is even, all elements must be even
        return all(x % 2 == 0 for x in nums1)
