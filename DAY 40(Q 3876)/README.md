# **3876. Construct Uniform Parity Array II**



You are given an array nums1 of n distinct integers.



You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.



For each index i, you must choose exactly one of the following (in any order):



nums2\[i] = nums1\[i]​​​​​​​

nums2\[i] = nums1\[i] - nums1\[j], for an index j != i, such that nums1\[i] - nums1\[j] >= 1

Return true if it is possible to construct such an array, otherwise return false.

&#x20;

# **MY EXPLANATION-**



This is a sequel question of the last one we did, but the main catch here is that this time odd and even number should be strictly positive non zero only.

Lets understand one thing , "ODD - EVEN = ODD" and "EVEN - ODD = ODD"
So if we know the smallest number in the array we can get our answer easily.
If the smallest number is odd , the answer will always be true because by the two formula i told you above we can turn any even numbers in the array into odd
But in case of smallest even number , that number cant be subtracted so every other number should be even too , so thats why we will check that condition using all() operator .

and hence we will get our answer

