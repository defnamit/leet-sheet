# **877. Stone Game**



## Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles\[i].

## 

## The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

## 

## Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

## 

## Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.





## **EXPLANATION-**



**Simple answer is Alice will always win!
HOW? See here only even numbers of piles exist , so if compute mathematically largest sum of all stones will either lie in the odd indexed stones or even indexed stones , if they both are playing optimally they can calculate in advance whether to choose even numbered (starting from first stone) or odd numbered (starting from last stone), so first player alice will always win.**



