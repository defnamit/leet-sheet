# **3498. Reverse Degree of a String**



Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:

For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
Sum these products for all characters in the string.
Return the reverse degree of s.


# MY EXPLANATION-



We will be using ord() in-built python function here .
Basically ordinal of every keyword is unique , and is uniformly assigned to each keyword.
For example- ord(a) = 97 and ord(z) is 122 , so we know there is exactly the difference of 26 as per the requirement of question.


Now to get the position of the string in revered index , we will use the position of last alphabet that is "z" and subtract it by the current alphabet that is s[i]+1 , we will get to know its index from opposite side , and from the front side , we already know the index that is i+1 (current iteration + 1).


Thats it , you will get your final answer.