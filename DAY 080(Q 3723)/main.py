class Solution:
    def maxSumOfSquares(self, num: int, summ: int) -> str:

        l=[0]*num
        i=0

        while(summ!=0):
            if(i==num):
                return ""
    
            if(summ>9):
                l[i]=9
                summ-=9

            else:
                l[i]=summ
                summ-=summ

            i+=1

        ans=str("".join(map(str,l)))
        if ans: return ans









