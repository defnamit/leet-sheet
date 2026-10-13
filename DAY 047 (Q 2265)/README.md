# **2265. Count Nodes Equal to Average of Subtree**


Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 


# MY EXPLANATION-


          
It is very simple but let me clear you if you encounter any question related to binary search tree (bst) , the first thing you need to create is a recursive function , this makes the whole process lot more easier.


Although bst is a vast topic , if you dont know the basic concepts, it will be little confusing but i will try to make it understand in simple steps .


Ans variable is created to store final ans , and nonlocal is used inside the function to make the variable global , so that ans variable doesn't changes on every recursion.


For every recursion main thing is base condition , and here we will stop if we encounter none as root.


Assume we will be using four pointers (left_sum , left_count , right_sum , right_count) , we will use left pointers to reach till the end of left side of the tree (leaf node) and plant both of our left pointers at that node , same will do for the right pointers.


Now the main game starts , total_sum will count the value for current node + for the left pointer who is pointing at the nodes (either left or right) , after this recursion is completed the pointers will move from leaf nodes , and will start moving toward root, and in that process we will add the values for each node.


Now pointers for left and right count will perform same action , but instead we dont want them to count values , but instead we want to know how many nodes are there in the current bst , so that is why we are adding +1 on each recursion , because as the pointers will head towards the root , total count will increment by +1.


At last we will be performing the basic mathematical operation to evaluate average. 