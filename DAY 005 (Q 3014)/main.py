class Solution(object):
    def minimumPushes(self, word):
        l=len(word)
        if(len(word)<=8):
            return len(word)
        else:
            n1=len(word)//8
            n2=len(word)%8
            c=0
            for i in range(n1+1):
                c+=8*i
            return c+((n1+1)*n2)
        
