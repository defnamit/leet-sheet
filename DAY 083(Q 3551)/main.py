class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        l=[]
        for i in range(len(nums)):
            s=sum(list(map(int,str(nums[i]))))
            l.append((s,i,nums[i]))

        new=sorted(l, key=lambda x:(x[0],x[2]))
        reach=[False]*len(nums)
        swaps=0


        for i in range(len(nums)):
            if reach[i] or new[i][1]==i:
                continue

            cycle_len=0
            j=i

            while not reach[j]:
                reach[j]=True
                j=new[j][1]
                cycle_len+=1

            swaps+=cycle_len-1

        return swaps

            
