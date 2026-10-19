class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        l=[]
        
        def merge(nums,left,right,mid):

            i=left
            j=mid+1
            temp=[]

            while(i <= mid and j<= right):
                if(nums[i] <= nums[j]):
                    temp.append(nums[i])
                    i+=1

                else:
                    temp.append(nums[j])
                    j+=1

            while(i<=mid):
                temp.append(nums[i])
                i+=1

            while(j<=right):
                temp.append(nums[j])
                j+=1

            for i in range(len(temp)):
                nums[i+left]=temp[i]


        def mergesort(nums,left,right,n):

            if(left>=right):
                return

            mid=(left+right)//2

            mergesort(nums,left,mid,n)
            mergesort(nums,mid+1,right,n)

            merge(nums,left,right,mid)


        n=len(nums)
        mergesort(nums,0,n-1,n)

        for i in range(len(nums)):
            if(nums[i]==target):
                l.append(i)

        return l
