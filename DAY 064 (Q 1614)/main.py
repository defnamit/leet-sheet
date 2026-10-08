class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        depth=0
        
        for i in s:
            if i=="(":
                count+=1
                
            elif i==")":
                depth=max(count,depth)
                count-=1
                
        return depth
