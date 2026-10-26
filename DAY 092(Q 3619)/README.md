# **3619. Count Islands With Total Value Divisible by K**


You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.


# MY EXPLANATION-


It is again a dfs problem we solved previously , and that too island related question.

Here the water is 0 , and land is non zero integers.


We will use dfs , where the base case is the same boundary case , for i and j , also if we reach at water (0) , then we will return 0.

we will store the value of grid[i][j] , because we need sum , and also mark that particular loc as visited , by assigning a 0.


Main thing is we will move up and down , if there is water or land , we will fetch their value accordingly , and add them in our variable s. At last we will return s .


Now in main func , we will iterate in the grid to find , the non zero number , will run a dfs from that location , and the sum dfs return is divisible by k , then we will increase our count (THAT IS WHAT THE QUESTION DEMANDED).