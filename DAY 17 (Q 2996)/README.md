## **2996. Smallest Missing Integer Greater Than Sequential Prefix Sum**





**You are given a 0-indexed array of integers nums.**



**A prefix nums\[0..i] is sequential if, for all 1 <= j <= i, nums\[j] = nums\[j - 1] + 1. In particular, the prefix consisting only of nums\[0] is sequential.**



**Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.**





## **MY EXPLANATION-**



**The question already states that sequential prefix (eg 1,2,3) starts from 0 index only make this question a lot easier.
We will define a starting point for our prefix storing the value nums\[0].
The first while loop will calculate sum of all the sequential prefixes, then we will create a set that will remove duplicate values as well as reduce time complexity too.
Then the second while loop is just to find that there exist the summed value in the list if yes then increase the summed value by 1 until we get our final answer**

