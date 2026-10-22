class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def valid(values: List[int]) -> bool:
            inv = False 

            for i in range(1, n): 
                if values[i] < values[i - 1]:
                    if inv:
                        return False 
                    
                    inv = True 

            return (not inv) or (values[0] > values[n - 1])

        ans = 10**9 

        if valid(nums):
            i = nums.index(0)
            ans = min(i, n - i + 2)

        rev = nums[::-1]
        if valid(rev):
            i = rev.index(0)
            ans = min(ans, 1 + min(i, n - i))
            
        return ans if (ans < 10**9) else -1 
