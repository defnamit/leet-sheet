# **200. Number of Islands**


Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# MY EXPLANATION-


1) Get to know the length of rows and columns of the grid.

2) Run a for loop first , to find our first 1 , when we find that definitely it will increment 1 in count , but also we will run a recursive function too.

Why recursive function? Our main aim is not only to find the 1 , but also to find all the 1 that are horizontally or vertically connected to that 1 , because all that contributes to 1 island .

And we are making it 0 , to basically neutralize them , so next time we visit that spot so we dont count it as a new island , as it is already contributed as an island previously.

What is base condition trying to say ? It is basically checking if the boundaries of i and j in range or not , and the pos we are currently in grid is actually 1 , because we want to neutralize 1 only .


Then we will recurse the function , by increasing i and j (horizontally and vertically).

And at last we will get our count of islands surround by the waaatteeeerr.