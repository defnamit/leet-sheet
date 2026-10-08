class Solution(object):
    def resultArray(self, nums):
        
        l1=[]
        l2=[]
        
        l1.append(nums[0])
        l2.append(nums[1])
        
        for i in range(2,len(nums)): 
            
            resultt=l1 if l1[-1] > l2[-1] else l2
            
            resultt.append(nums[i])
            
        return l1+l2
