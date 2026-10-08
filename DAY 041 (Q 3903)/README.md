# **3903. Smallest Stable Index I**





You are given an integer array nums of length n and an integer k.



For each index i, define its instability score as max(nums\[0..i]) - min(nums\[i..n - 1]).



In other words:



max(nums\[0..i]) is the largest value among the elements from index 0 to index i.

min(nums\[i..n - 1]) is the smallest value among the elements from index i to index n - 1.

An index i is called stable if its instability score is less than or equal to k.



Return the smallest stable index. If no such index exists, return -1. 





# **MY EXPLANATION-**



We will be using the pointer logic here , because if you analyze question deeply you will notice a pointer behaviour only because as the max is moving forward , resulting the min is shrinking.

So we will place a pointer at first index and a pointer at last.
We have to check condition until and unless our first and last pointer meet , that's what our while condition is trying to say.

And then we will write our main logic as per the question , and simultaneously increment our first pointer too.
And that's all.

