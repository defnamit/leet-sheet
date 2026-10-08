# **1563. Stone Game V**





**There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.**



**In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.**



**The game ends when there is only one stone remaining. Alice's score is initially zero.**



**Return the maximum score that Alice can obtain.**







## **MY EXPLANATION-**



**If you understand closely , we have to divide our given array of integers again and again , so best possible way we can solve is recursion , it will reduce the time complexity.
We will just run a for loop in arr , and for each loop we will create two new lists to store left value and right value , side by side comparing it with the cases. And yeah it will help us to reduce time complexity , hahahaha.
If you analyze properly , there will occur only three cases , left> or left< or maybe they are equal.
For left and right its easy , we will simply compare which has least sum because that will only be added in the Alice's total score.
And if you are confused why we used max operators in the if and elif blocks because Alice's final goal is to maximize her score only and that what our recursive function is told to do.**

