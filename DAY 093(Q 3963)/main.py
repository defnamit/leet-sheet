class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        l=[]
        
        for i in range(m):
            s=""
            for j in range(n):

                if(i!=m-1):

                    if(j==0):
                        s+="."
                    else:
                        s+="#"

                else:
                    s+="."

            l.append(s)

        return l

                    

