# **3517. Smallest Palindromic Rearrangement I**





## You are given a palindromic string s.

## Return the lexicographically smallest palindromic permutation of s.





## **MY EXPLANATION-**



**Lexicographically here means according to the dictionary order , means smallest to largest.
We have used counter here that stores the number of occurrence of each string in the form of key value pair.
If you wonder why we used left and middle here , we just have the prepare our string's left part and middle part and will join both the parts + reverse the left part and it will form our final output.
We will sort and divide the occurrence by two (in mirror halves) and append it in the left list and definitely if the occurrence is odd we should have its mirror part on left side + one remaining element in the middle too.
And in the last we will join them all and hence get our desired output**

