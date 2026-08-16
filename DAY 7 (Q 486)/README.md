# **486. Predict the Winner**



### You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

### 

### Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums\[0] or nums\[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

### 

### Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.









## **MY EXPLANATION-**





**Here both the players are playing optimally and they both are competing to win.
Players will decide they are winning or not is by calculating their score - opponents score , if its in positive they are winning , if negative they are loosing , so obviously they want to keep their score positive , that is why we will be using a recursive function, it will calculate all possible scores and give the final output score that will help the either players to keep their score positive , return max means same only , that will decide that what choice will make the player have max score.
return dfs(0, len(nums) - 1) >= 0 , this is used to return the output as true or false , if greater than 0 then obviously p1 is winner so true else false**







