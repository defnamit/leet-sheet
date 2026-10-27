# **3963. Create Grid With Exactly One Path**


You are given two integers m and n, representing the number of rows and columns of a grid.

Construct any m x n grid consisting only of the characters '.' and '#', where:

'.' represents a free cell.
'#' represents an obstacle cell.
A valid path is a sequence of free cells that:

Starts at the top-left cell (0, 0).
Ends at the bottom-right cell (m - 1, n - 1).
Moves only:
Right, from (i, j) to (i, j + 1), or
Down, from (i, j) to (i + 1, j).
Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.



# MY EXPLANATION-


What makes this ques easy is , that we can have multiple answers, because for this one we dont need any shortest path or like minimum kind of thing , so our approach will be very clear.


Although if you have any different approach its very fine , but i guess mine is easy too.


What will we do is , starting from top left corner all the way to bottom right corner we have to travel , so in my opinion the most basic route will be to go all the way down from the left corner , until you reach the last row , and then travel all the way to the right side.
(we will also fill the unused area with "#" , because that is what question says is , (EXACTLY ONE PATH)).

That is the most basic and easy travel , now will look how to code this.

Will create traverse in rows and columns , and if we are not in the last row , then our patter will only be ".######"..... and so on , that means the first column will be "." , and the unused one will be "#" , and when we reach at last row , then we obviously need to traverse only right side so will add "." till we reach the right corner.


AND THAT"S ALL , I HOPE YOU GOT IT..