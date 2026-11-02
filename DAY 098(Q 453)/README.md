# **453. Minimum Moves to Equal Array Elements**


Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.




# MY EXPLANATION-


So instead of solving this ques , as stated above , we will slightly flip the ques , because that will become much more easier for us to get to the ans.

It is told us to , increment smaller number by 1 to reach the larger number , but if we just choose the smaller number make that as a target and decrease each element one by one from target value we will get our suitable ans.

But you may ask that , ques clearly states to perform operation on n-1 elements at a time , but we are doing one by one !!


Let's dive in deep , if you calculate you will know something crazy , "increasing all elements to reach max has the same relative difference as decreasing one element at a time to reach min".

And this is the solid approach , that makes this one liner ans a medium ques .



Below is the one line answer (actually a derived one).