# **1254. Number of Closed Islands**


Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



# MY EXPLANATION-


We have already done a island related ques , already in the repo ( Q 200) , it is a same ques , with some minor changes , lets go through what question wants.


We want to tell number of isolated islands in this , and in that question we just wanted to count number of total islands.

Isolated islands are the one which are compulsorily captured around water (up , down , left , right) , this also means that the any part of the island should not touch the boundary of grid.


Now lets dive in the code , we have this dfs func , which gets activated when we encounter land (that is 0) , first if condition inside dfs is checking the boundary condition , that we dont go out of the boundary range , also it will return false if there is land(0) at the boundary.

How? So understand what dfs actually does , it just iterates in one direction until and unless the condition dissatisfies , so if dfs is following the direction of land , and it goes out of the boundary , that eventually means that there existed land at the boundary , because if not that then it will obviously returned True (read the second if condition).


Second if condition also emphasises on one very important thing , if we started from 0 and lands on water it will return True , (its important significance is mentioned below).


Now we will mark the current grid as 1 , because we dont want to iterate again and again on the places we have visited.


Comes the important part , dfs will recurse in all directions , and only return true , if all direction == True , so as i mentioned earlier , if we land on water , we will get True , so if we land on water from all directions ,that purely satisfies our question's demand , and eventually return true.



In the main function , we will run a for loop , and count +1 when we get true from dfs ( that counts total number of isolated islands).


THATS ALLL , WAS A LITTLE HECTIC EXPLANATION , I HOPE YOU UNDERSTAND , ELSE JUST MAIL ME BABY!