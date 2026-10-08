# **1872. Stone Game VIII**





**Alice and Bob take turns playing a game, with Alice starting first.**



**There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:**



**Choose an integer x > 1, and remove the leftmost x stones from the row.**

**Add the sum of the removed stones' values to the player's score.**

**Place a new stone, whose value is equal to that sum, on the left side of the row.**

**The game stops when only one stone is left in the row.**



**The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.**



**Given an integer array stones of length n where stones\[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.**



&#x20;

## **MY EXPLANATION-**





**I tried solving this using recursion but , you will definitely understand my approach too , and that too in less time complexity.
We created a suffix list , so as to store the sum of stones at each position or chance, lets suppose alice choses x=3 , so suffix will store the points she will gain choosing x=3.

Initially we will assume that the opponents winning point is ans, but in for loop we will be running a reverse loop , why? Because , we stored the sum of all points in suffix from left to right , but it may have max values at some index and min value at some index.
Alice only have to take max score , so we will be using max operator , and judge whether taking stones upto that position will have more score gain for alice , or the previous one (by subtracting prefix\[i]-ans)

Thats it , and you will get your final answer**

