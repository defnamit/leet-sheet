# **20. Valid Parentheses**



Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

# MY EXPLANATION-


Will follow a simple rule , that is "bracket that is opened last will be closed first."


So will create a stack , where we will append all opening brackets , but as we encounter a closed one , we will verify that is it the last bracket that was opened too , if yes then fine we can continue.

Else , this is an invalid type , and return False.

If at last stack is not empty , that means we still have opening brackets without its closing pair , so then too will return False.