# **940. Distinct Subsequences II**


Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.


# MY EXPLANATION-

Understand closely what i am trying to say , then this hard problem will look easy to you or maybe a mid, what so ever.


Listen the abstract idea , here we are distributing or charecters in an array (dp) in such a way , (just assume a linear line of a graph for a sec) , and that is how are distribution is gonna be , every new element will be placed in the array but also will be appended to an existing substring previously got formed or added in the substring.


That is what our code is doing , read my abstract idea 2 to 3 times , and then when i will explain my code , you will feel eazzzz.

Dp array for 26 zeroes is created because of 26 alphabets a string can contain, and the indexes in the dp will tell us the index of that char which gets ended (or at the last position ) in the particular substring.
(Read the just next para to understand this example better , for eg --> dp[0] =4 , that means there are 4 substrings that ends with a)

Will run a for loop , and inside the for loop we will fetch the index of each char according to the alphabetical order (for eg = a(1) , b(2) , c(3) and so on) , and the best way is to use ord() function.

Here Total is fetching the total existing subarrays + 1 (1 is added because the char itself can be a substring too).


Now we will update our dp[i] , i is that particular index i just told , and updating total means there are these many substring that ends with that char.


At last we will return sum of dp , because it will tell us all the possible subarrays.