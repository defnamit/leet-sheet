class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        i=0
        d={}

        for key,val in knowledge:
            d[key]=val
    
        n=len(s)
        string=""
        result=""

        while(i!=n):
            if(s[i]=="("):
                i+=1

                while(s[i]!=")"):
                    string+=s[i]
                    i+=1
                i+=1

                if string in d:
                    result+=d[string]
                else:
                    result+="?"

                string=""

            else:
                while(i<n and s[i]!="("):
                    result+=s[i]
                    i+=1

        return result

        


            
                
                
                    
        
