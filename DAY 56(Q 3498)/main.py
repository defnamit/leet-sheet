class Solution:
    def reverseDegree(self, s: str) -> int:
        
        sum=0
        for i in range(len(s)):
            
            sum+= (ord("z")-ord(s[i])+1) * (i+1)

        return sum
