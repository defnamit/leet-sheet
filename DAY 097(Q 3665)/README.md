# **3665. Twisted Mirror Path Count**


Given an m x n binary grid grid where:

grid[i][j] == 0 represents an empty cell, and
grid[i][j] == 1 represents a mirror.
A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

Since the answer may be very large, return it modulo 109 + 7.

Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.



# MY EXPLANATION-



We have to find multiple paths , the best and most appropriate module we can use is lru_cache and that is the decorator defined above the dfs func.


What does lru (least recently used) cache , used for memorization actually is doing in this code?

So we are given to find multiple paths , and that can happen only when we do not move on that same paths again and again , and how does lru cache will be preventing this? It just stores the memory for each function , let us suppose we are in the state dfs(1,2,"down") and to reach we need 5 steps , so it will store that data as memory , so the next time recursion is called all over from start and reaches that same state , so it doesn't calculates all step over again it ignores remaining operations and return the result stored in the memory (if needed).


Likewise here too , the dfs will move in the directions and will remember the states from where it can reach the end , that will conclude that this path is valid.


Now in the code , we will be using variable direct for to specify directions , because without that it will be difficult to know whether the 1 i am standing into right now , i came from which direction , and for this ques direction will play an important role.

1. The `if` condition inside the DFS is the boundary condition. You know it very well.
2. The `if` condition is the base condition, or you can say an ending condition: if we reach the final cell we will return 1. That means `true`. That means we have found the valid path.
3. As the question states, if we encounter 1 (that is, a mirror), and if we encounter it from the right side, we'll go down. If we encounter it from the down side, we will go right. That's what our third `if` condition is trying to do. The last `return` condition is the most important thing to understand: what it is trying to say. We have to return the number of unique paths. That's why we are returning `DFS` first in the right direction and down direction. First we will propagate from the right and count all the sequences that can return `true` or can be considered as a valid path if we start propagating from the right direction. Then we will add all those paths. We are returning 1 again and again and we will add all those 1s with all the propagation that will happen when we propagate in the down direction.