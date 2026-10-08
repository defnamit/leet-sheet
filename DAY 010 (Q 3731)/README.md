# 3731\. Find Missing Elements





You are given an integer array nums consisting of unique integers.



Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.



The smallest and largest integers of the original range are still present in nums.



Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.



# **MY EXPLANATION-** 



Ezzzzz , so basically we have to identify the largest and smallest element in the list and then find the missing numbers that exist between these two range.
We will create an empty list to store the missing values and the  store the maximum and minimum values too using min max function, then run a for loop running from min value to max and using "not in" operator to identify the missing values and then finally append in the empty list we created.

