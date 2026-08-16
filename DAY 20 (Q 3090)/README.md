# **3090. Maximum Length Substring With Two Occurrences**





### Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.





### EXPLANATION-



Here we will be using two pointers , LEFT and RIGHT , our main idea is to increase our right pointer in forward direction , and when the condition does not satisfies shrink the length using our left pointer.

Like in this case , here we have an empty dictionary , using right pointer we will store every occurrence of the elements and when the occurrence gets bigger than 2 , we will then shrink the list using our left pointer.
The max operator then will judge and can figure out our final output that is length of substring.




