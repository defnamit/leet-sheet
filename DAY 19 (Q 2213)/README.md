## **2213. Longest Substring of One Repeating Character**



#### You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

#### 

#### The ith query updates the character in s at index queryIndices\[i] to the character queryCharacters\[i].

#### 

#### Return an array lengths of length k where lengths\[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.



# 

# **MY CODE EXPLANATION-**



##### The key idea behind using a Segment Tree for this problem is that finding the longest sequence of repeating characters across a full string can be broken down into smaller sub-problems across contiguous ranges.

##### 

##### When you divide a string in half, the longest repeating substring in the combined range comes from one of three possibilities:

##### It lies entirely within the left half.

##### 

##### It lies entirely within the right half.

##### 

It crosses the boundary between the left and right halves.


---



&#x20;

