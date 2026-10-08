# **3345. Smallest Divisible Digit Product I**



#### You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.





## **MY EXPLANATION-**



**Here we will first separate all numbers of the integer value n in the list using , list(str(abs(i)))**

This will just simply help us to perform multiplication on the elements easily but yeah i do agree it can increase time complexity too but you can have a different approach.


So then we will multiply the elements of n first , because it may be divisible by t , if it is not we will increment the n and do same work again and again until we find our first divisible number by t.









