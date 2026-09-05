# **3904. Smallest Stable Index II**





You are given an integer array nums of length n and an integer k.



For each index i, define its instability score as max(nums\[0..i]) - min(nums\[i..n - 1]).



In other words:



max(nums\[0..i]) is the largest value among the elements from index 0 to index i.

min(nums\[i..n - 1]) is the smallest value among the elements from index i to index n - 1.

An index i is called stable if its instability score is less than or equal to k.



Return the smallest stable index. If no such index exists, return -1.





# **MY EXPLANATION-**



If you wonder , yes it is the exact same question as the previous one , but if you will look in constraints , you will know this question will have length of integer upto 10^5 , so basically you have to solve this question now with different logic so as to minimize the time limitation.

My previous solved ques will not help you this time , because that method was definitely the brute force.
Now this will be the good approach i solved for this question

If you wonder what suffix\_min is here , so basically we will be storing every minimum values that will be possible on each index , (For eg- from index 2 to the nth index minimum value is X , that's what the suffix\_min\[2] will be storing)

And rest using pointer , max method is same as that of previous one.

This suffix method will be saviour for many questions if you understand this method, this saved us in this question too.

And that's all.

