# **3875. Construct Uniform Parity Array I**





**You are given an array nums1 of n distinct integers.**



**You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.**



**For each index i, you must choose exactly one of the following (in any order):**



**nums2\[i] = nums1\[i]**

**nums2\[i] = nums1\[i] - nums1\[j], for an index j != i**

**Return true if it is possible to construct such an array, otherwise, return false.**



&#x20;

# **MY EXPLANATION-**



Ah an easy question (literally) hahahah
So just think that if the question is giving us the freedom to subtract the number with any number present in the array , then subtracting two odd numbers you can create one even too , and subtracting an odd from even you can have an odd number too

Soo very easy , it will always return True.

