class Solution:
    def sumCounts(self, s: List[int]) -> int:
        
        l=[]
        count=0

        for i in range(len(s)):
            for j in range(i):

                if(s[i] not in l[j]):
                    l[j].append(s[i])
                count+=len(l[j]) ** 2
                    

            l.append([s[i]])
            count+=1

        return count
