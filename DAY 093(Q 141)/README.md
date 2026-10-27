# **141. Linked List Cycle**


Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



# MY EXPLANATION-



The very famous ques is here , i am damn sure you have already watched its solution on reels or yt short only , because i had , if not then let's dive in.

So we have to find a cycle , if you think logically keeping the code aside , assume two friend's are walking on a circular path , if one will start walking fast than the other surely it will move head from him , but the main thing is they will surely meet after some certain time , because the one moving fast is reducing the total distance between them fastly.

Here we doing the same thing , two pointer's will be roaming on a trip , one slowly as "slow" and one "fast" , in the while loop , if the fast reaches a null point , it will automatically return false.

While the slow jumping only one node at a time , fast one is jumping two nodes at a time , if they meet , return True.