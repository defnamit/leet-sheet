# **3016. Minimum Number of Pushes to Type Word II**



### You are given a string word containing lowercase English letters.

### 

### Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with \["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

### 

### It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

### 

### Return the minimum number of pushes needed to type word after remapping the keys.

### 

### An example mapping of letters to keys on a telephone keypad is given below. Note that 1, \*, #, and 0 do not map to any letters.





## **MY EXPLANATION-**



**Here the catch from previous day ques is , the element can be repeated here too , so our first basic approach will be to make priority the element who has more number of repetition so we can minimize our pushes.**

**Thats why we used sorted in the counter to know the max repeated value, using enumeration then we will know the position of the value and how many times it repeated because that will contribute in our final number of pushes.
pushes = i // 8 + 1 , this explains that the pushes will depend on the divisibility of 8 , for eg if there are under 8 elemenents in string then 1 pushes for all , if under 16 then 2 pushes and so on.**



