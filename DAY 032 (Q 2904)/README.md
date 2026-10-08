# **2904. Shortest and Lexicographically Smallest Beautiful String**



**You are given a binary string s and a positive integer k.**



**A substring of s is beautiful if the number of 1's in it is exactly k.**



**Let len be the length of the shortest beautiful substring.**



**Return the lexicographically smallest beautiful substring of string s with length equal to len. If s doesn't contain a beautiful substring, return an empty string.**



**A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.**



**For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.**







# **MY EXPLANATION-**





**We will be using map() function to convert string into list.
And we will be running to for loops so as to get our beautiful substring , we used sum operator because question asked us that beautiful substring should have k number of 1 , logically if we do sum of that substring that will be also equal to 1.
To check if its lexicographically small or not =(current < out)
If our output(out) is equal to the s\_list and also if sum is not equal then definitely no beautiful substring exists for our condition , so we will be returning "".
And hence we will be getting our desired output.**



