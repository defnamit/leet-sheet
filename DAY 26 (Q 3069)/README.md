# **3069. Distribute Elements Into Two Arrays I**



### **You are given a 1-indexed array of distinct integers nums of length n.**

### 

### **You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums\[1] to arr1. In the second operation, append nums\[2] to arr2. Afterwards, in the ith operation:**

### 

### **If the last element of arr1 is greater than the last element of arr2, append nums\[i] to arr1. Otherwise, append nums\[i] to arr2.**

### **The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == \[1,2,3] and arr2 == \[4,5,6], then result = \[1,2,3,4,5,6].**

### 

### **Return the array result.**













# ***MY EXPLANATION-***





**First approach you will always have to take is insert first and second element in the list 1 and list 2 , as it is mentioned without any condition.
Then we will iterate after the second position obviously to the end of list and check which list among have the largest element in its last block and easily we will get to know which list it is,
and then using the append function we will add that ith element of nums and simply having 0ms run time you will have your answer adding both the list and 2.**

