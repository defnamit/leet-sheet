class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        d={}
        for key,val in knowledge:
            d[key]=val
            
        string=""
        result=""
        cas=0

        for i in range(len(s)):
            if (s[i]=="("):
                cas=1

            elif(s[i]==")"):
                cas=0
                if string in d:
                    result+=d[string]
                else:
                    result+="?"
                string=""

            elif(cas==1):
                string+=s[i]
            
            elif(cas==0):
                result+=s[i]

        return result


        


            
                
                
                    
        
