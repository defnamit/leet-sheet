class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        stack=[]

        for i in s:
            
            if(i=="("):
                stack.append(i)

            else:
                if(stack):
                    stack.pop()

                else:
                    count+=1

        return len(stack)+count
