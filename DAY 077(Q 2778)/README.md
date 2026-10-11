# **2778. Sum of Squares of Special Elements **


You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums.
 


# MY EXPLANATION-


I dont think so , this need an explanation , but ahh shit here we go again.

So basically we have given an one indexed list not 0 (because 0 cant be divided) , and we have to find the squared sum of all the number whose index is divisible by length of list.

Will directly use sum operator, and will iterate from 0 to n , but while dividing we will add +1 in i , because as mentioned in question it is 1 indexed array.