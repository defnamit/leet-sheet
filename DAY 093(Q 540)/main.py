class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        head=0
        tail=len(nums)-1

        while(head!=tail):
            mid=(head+tail)//2
            if(nums[mid+1]!=nums[mid] and nums[mid-1]!=nums[mid]):
                return nums[mid]
                
            if(mid%2==1):
                if(nums[mid]==nums[mid-1]):
                    head=mid+1
                    continue
                else:
                    tail=mid
            else:
                if(nums[mid]==nums[mid+1]):
                    head=mid+2
                    continue
                else:
                    tail=mid

        return nums[head]
                
