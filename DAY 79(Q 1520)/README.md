# **1520. Maximum Number of Non-Overlapping Substrings**


Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

 


# MY EXPLANATION-

Long ahh typing bruhh , lesgooooooo-

So let me tell you my approach in abstract way ->

so basically we will create dictionary named first and last , in first loop we are basically storing each possible character in these dictionaries , with the index of first occurrence of that char in the string will be stored in first dict , and the last occurrence index in the last dict.


Now we will store the intervals of all the valid substrings (according to the situations given to us in the question).


Will pick each character from either of the dictionary , and use two pointers , one to point at the first occurrence of that character and second to point at the last occurrence . 

(Why are we caring for first and last occurrence together? because in question it clearly states that if you take a char in the substring then all of its occurrence should be there in the same substring , so to find the suitable substring we have to take first and last because in between them all of that particular character lies.)


We wil be running loop from the starting index till the last index of that char.


Notice the if statement , so basically it tells us to ignore that char whose first occurrence lies beyond the left most of the starting index (understand that we cant choose that char in substring whose all occurrence doesn't lies in that particular bound we are iterating , and in this case too the question will contradict so we will immediately exit the for loop)


We will also be expanding our right pointer , if the last index of the current char is beyond our existing r pointer , because it is our greedy approach to include every valid substrings initially then evaluate them later to get the correct answer, and if the flow is happening to be in valid form then we will definitely expand our pointer to include every valid substrings.


And at last when our while loop end we add the valid left and right pointer index to the interval array.


Now we are heading towards main thing , notice we sorted our interval array BUT on the basis of the last index (WHYYYYY?? Because questions demands from us to return the maximum number of substrings that meet the above conditions, and if any substring is ending very early (or at very short index) , then we definitely have gates opened to insert more and more valid substring , that is why we are prioritizing the substring with less ending index).


Now we will append the final answers in the ans list , based on only one condition that the first index and last index of all our valid substring doesn't clashes , as mentioned in the question The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true. (The whole for loop in last is doing the same as i mentioned).



And then we fill ahhh finally return our ans list , and lesgooo we did it all.