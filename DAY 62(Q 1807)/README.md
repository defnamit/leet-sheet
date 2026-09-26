# **1807. Evaluate the Bracket Pairs of a String**



You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:

Replace keyi and the bracket pair with the key's corresponding valuei.
If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

Return the resulting string after evaluating all of the bracket pairs.


# MY EXPLANATION-



So our first step is here to convert the list knowledge into dictionary d, with first element as key and second element as value pair inside dict ( because it will be easy for us to perform searching operating) .

We will be using for loop , with some multiple cases.

We have to identify that are we inside the bracket or outside the bracket(cas ==1 if inside else cas==0)

If we are inside the bracket , we will form the string , and as the bracket closes we will immediately verify that is that string exists in the dict or not , if it exists we will add that replacement word in the result string.

And at last we can print the result.