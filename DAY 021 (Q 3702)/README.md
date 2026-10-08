# **3702. Longest Subsequence With Non-Zero Bitwise XOR**





## You are given an integer array nums.

## Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.





### **MY EXPLANATION-**





First of all you have to know that the possible answers that can be taken will only be , "len(nums) , len(nums)-1 , 0".
why? Because know that xor of any number with 0 = 0 
answer will be 0 only if all the elements equals to 0, thats what line 11 means.

