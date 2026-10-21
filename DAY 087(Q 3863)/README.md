# **3863. Minimum Operations to Sort a String**


You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.



# MY EXPLANATION-


I believe in this question you dont actually need the dsa knowledge in that extent , if you have some big big brain , then i guess you could hahahahah.


I guess you now why are we returning 0 , if the string is already in its sorted form , then we dont need to do anything , then a 0.

If length is 2 , it is impossible to sort , because you know ques says you cant select the whole string , and for 2 length , you cant fuck around anything taking a single length substring , so keep it out of your hand broski.


Comes the main part , we will get the minimum substring alphabet and maximum too , and if you apply your brain , if first is small or last is the max , we actually need 1 step to sort the rest , because first or last is already in its place also we can't choose the whole string as substring , so we left with obviously n-1 substring , and we can sort them in 1 go.


The second if says , if any of the min and max comes in between the boundaries then the answer is obviously 2 , 1 sort needed to arrange from the first and second from the last.


The main question may come in your big brain ? If the min and max are not at the boundaries so , it will definitely exist inside the boundaries , so this will always return 2 !!! Isn't it?


NOOOOOOO , here comes a twist , what if the largest element is at the first position , and the smallest one at the last index , it is almost sorted in descending order but we wanted an ascending order , in that case we obviously need 3 sortings , WHY???  

Because you need to bring the first element completely at last , and last to the first , so our logic for the above if condition will not fit , we definitely need to arrange first and second halves in 2 steps , but one step additional for this whole movement i told.



It was a funnnn question , isn't it?
