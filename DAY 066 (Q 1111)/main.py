class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        n=len(seq)
        output=[0]*n
        depth=0

        for i in range(len(seq)):

            if(seq[i]=="("):
                depth+=1
                if(depth%2==1):
                    output[i]=0
                else:
                    output[i]=1

            else:
                if(depth%2==1):
                    output[i]=0
                else:
                    output[i]=1
                depth-=1

        return output


            

    
