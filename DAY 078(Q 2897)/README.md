# **2897. Apply Operations on Array to Maximize Sum of Squares**


You are given a 0-indexed integer array nums and a positive integer k.

You can do the following operation on the array any number of times:

Choose any two distinct indices i and j and simultaneously update the values of nums[i] to (nums[i] AND nums[j]) and nums[j] to (nums[i] OR nums[j]). Here, OR denotes the bitwise OR operation, and AND denotes the bitwise AND operation.
You have to choose k elements from the final array and calculate the sum of their squares.

Return the maximum sum of squares you can achieve.

Since the answer can be very large, return it modulo 109 + 7. 


# MY EXPLANATION-

Our abstract idea is to stretch the integer number into its binary form in a binary scale and combine all the bits lying on the same scale to get the greatest number and then add em.

Why we built cnt as 31 size 0 array , because of constraint mentioned below the question directs us.
Cnt variable is an array to store every bit of the binary number , for eg cnt[0]=1, cnt[1]=2 , cnt[2]= 4 and so on , i hope you understood what i am tryin to tell yall.

First for loop is just to pick every number in the array nums, and basically this method is used to distribute int into binary scale (as mentioned above) , we basically compress the number (move it to the right side using right shift operator) and see if at the last position is there binary 1 (using and operator with 1) , this allows to tell at which binary bit positions we have our switch on's (1) and at only that position we will increment our cnt array by +1.


Second for loop will iterate from 0 to k'th time , here our basic fundamental is that we already have cnt array which contains the record of all int in its binary form , here we are just adding it in a loop by using right shift and binary or operator , and finally storing that in ans after squaring the sum (that is stored in x) , because basically or operator with shifts are used to add two binary numbers , and we will repeat this process for k times to get our final answer.
