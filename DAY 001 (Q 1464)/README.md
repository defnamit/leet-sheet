# **1464. Maximum Product of Two Elements in an Array**





### Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums\[i]-1)\*(nums\[j]-1).







## **MY EXPLANATION-**

&#x20;



**Our main aim is to take the maximum output from the list from this formula, (nums\[i]-1)\*(nums\[j]-1).**

**So our main idea will only be to find the two largest elements from the list.**

**Firstly we will initialize both first and second largest elements as 0, and then traverse the whole list , finding the number greater than the first largest number , we will shift the assignment of first to seconds largest number and will do so on for the entire list.
And hence we will get the output.**

