# **2089. Find Target Indices After Sorting Array**


You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.




# MY EXPLANATION-


If you wondering , how the heck this long code for this easy problem , so i just wanted to try merge sort method to sort , because its time complexity is just (n log n).


I assume you don't need to know how this sorting works , little bit complex because it mainly involves backtracking method , if you want you can definitely sort directly using function sort() or sorted().

Then you can use for loop , to detect the target and its index , store the indices in a separate list , and then just return the list.
