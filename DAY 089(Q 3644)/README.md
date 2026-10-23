# **3644. Maximum K to Sort a Permutation**


You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.



# MY EXPLANATION-


Firstly i want to say that , how stupid this question is!

But here he have given an permutated array , and you have to swap the two number which are not placed properly and have to return the bitwise and of that number (k).

In ques if you look , we have denoted c =-1 , because & operation of any number with -1 gives the same number.
We will do and operation with all the number that are misplaced , and notice one crucial thing , that is we can only swap one pair because we want to return a single value for k .


If you analyze closely for this code , then you will know if more than one incorrect misplaced pair will be encountered , c will become 0.

