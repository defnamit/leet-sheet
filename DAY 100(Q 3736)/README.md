# **3736. Minimum Moves to Equal Array Elements III**



You are given an integer array nums.

In one move, you may increase the value of any single element nums[i] by 1.

Return the minimum total number of moves required so that all elements in nums become equal.



# MY EXPLANATION-


The ques we solved in day 99 , this one is similar with that , but with 1 difference , here we are only allowed to increase the numbers to balance the array.

In the case we have to increase , we left with only one option that is , take the max number as a target , because if we take any other number , we have to decrease the larger one (that is not allowed).

WE will run a for loop in the array , and we will count the difference of the particular element with the target element (target = max(nums)) , the difference between them is the as many steps we need to balance the array.

And at last we will return count.