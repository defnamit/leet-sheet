class Solution(object):
    def smallestNumber(self, n, t):
        ll=float('inf')
        i=n
        while True:
            product=1
            d_list=list(str(abs(i)))
            for j in d_list:
                product*=int(j)
            if(product%t==0):
                return i
            else:
                i+=1
