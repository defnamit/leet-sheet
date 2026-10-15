# **2913. Subarrays Distinct Element Sum of Squares I**


You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.



# MY EXPLANATION-


You can consider it as a mid easy question , but even if you can go for the brute force method , it still be acceptable because of its constraints given.


So here we are going with brute force (O(n2)) , our basic approach is we will create a nested list , and append the numbers to an existing numbers present in the list , to create a new new distinct subarrays.

For eg --> nums =[1,2,1]

first we will append 1 , and increase for its count , then when the pointer reaches 2 , the previous subarray was 1 , now adding 2 with 1 create a distinct subarray [1,2] and 2 alone creates a subarray [2], and this process will continue to iterate and we will get our count on the basis of len of that nested list and squaring them.


I know it is bit confusing , but i think i can explain better on digital board / copy pen!