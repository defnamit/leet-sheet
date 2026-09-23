# **1658. Minimum Operations to Reduce X to Zero**



You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.



# MY EXPLANATION-



Understand why we did target=sum(nums) - x, because here instead to delete the x number we will keep the numbers except x , and conceptually both means same.


If target is in nums , that means x does not exist in nums , so return -1.


if target == 0 , that means sum = x , and that also means to return every number that is len(nums)


Now we will create a slider window for this question where left will point to the first element and move towards the right , curr is the sum of that window (window = left pointer to curr pointer).

We will start from left , and add all the element until curr slider becomes greater than the target value , if it becomes greater will will shrink our slider using left pointer , simultaneously subtracting the numbers from left, as to satisfy the situation.


If the window(curr) becomes equal to target value , we have to keep the length of longest window , why? because question asks us to remove minimum element so which is equivalent to keep the largest subarray or window, and in the last line it clears your doubt that subtracting the longest length from the length of array we get the minimum elements to be removed.


