# **1569. Number of Ways to Reorder Array to Get Same BST**


Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.



# MY EXPLANATION-


A little bit tricky yet a simple bst problem , and this is our second bst problem , here we go again.


Main abstract idea to solve this question will be , will take the parent node from each root of the tree (left child , right child) . And create two list , because as we know the larger number goes to the right side of the node , and the smaller one on the left , for the same logic we will get all the child nodes for that particular parent node in a function.


Our main thing for the question is the formula , we will definitely use formula for combination , where we will calculate all possibilities from the given total nodes.

So total node = nums-1 (-1 because the parent root's position will always be same , we just have to change the order of their child nodes) , and r in combination will be len(l) , (That means we have to create possibilities from total number of child nodes , with respect to the length of either child node).


And then we will recurse our function , because we need total number of combination for the left node as well as right node.


I hope you understand , and i hope you also understood why in the last line i wrote -1 , because the total number of combinations is calculated using the one given in the testcase ques , we have to exclude that one . HEHEH
