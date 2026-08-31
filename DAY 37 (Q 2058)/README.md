# **2058. Find the Minimum and Maximum Number of Nodes Between Critical Points**





**A critical point in a linked list is defined as either a local maxima or a local minima.**



**A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.**



**A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.**



**Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.**



**Given a linked list head, return an array of length 2 containing \[minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return \[-1, -1].**





# **MY EXPLANATION-**


This is my first encountered linked list ques , and very lovely question , hahah

Lets make u understand some basic things , to traverse in linked list , there is a basic requirement to have minimum of one temporary variable , so here we are using , "temp" and "prev".

Temp will point on the second element on the list (because critical point can't be in the start or end of the list) and prev is used to store last value of temp , because it is single linked list and it is important for us to have the record of last value to know the critical points.

We will run a while loop , until temp.next=NULL and if loop to identify critical points , and storage is a list variable to store the positions of all that points.

To reduce time complexity , we will find our minimum distance of two critical points inside this if loop only .
We have prev\_pos , to store the position of previous critical points , it will be then easy for us to perform subtraction and find minimum distance.

prev\_pos != 0:, This condition is important to understand , so if you look closely we are assigning prev\_pos = pos , so in the first iteration prev\_pos=0 , and we dont want our minm to be 0 because then it will be of no use if you understand it logically.


maxm = storage\[-1] - storage\[0], this is the basic concept , in the list maximum distance logically will be the first and last position only.






