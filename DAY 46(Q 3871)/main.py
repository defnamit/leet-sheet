class Solution:
  
    def countCommas(self,n:int)->int:
        c=0
        p=1000

        while(p<=n):
            c+=n-p+1
            p*=1000

        return c
