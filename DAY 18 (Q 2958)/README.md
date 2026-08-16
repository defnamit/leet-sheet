## **2958. Length of Longest Subarray With at Most K Frequency**





#### You are given an integer array nums and an integer k.

#### 

#### The frequency of an element x is the number of times it occurs in an array.

#### 

#### An array is called good if the frequency of each element in this array is less than or equal to k.

#### 

#### Return the length of the longest good subarray of nums.

#### 

#### A subarray is a contiguous non-empty sequence of elements within an array.









# **MY CODE EXPLANATION-**



**Here I used two pointers left and right , my main aim is to find the largest window we can consider as a subarray.
Making my left pointer initially stable at 0 and making my right pointer move to the right side from the beginning of the array .
Use of right pointer is just to count the occurrence of numbers , and use of left pointer is to shrink the array (or reduce occurrence of the number which is greater than k) in while loop, because it will remain a continuous process until our demands are satisfied.
At last we will use max operator to actually judge the final length of the subarray.
Thats it.
THANKYOU**

