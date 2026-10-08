class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for n in s:
            if n in "([{":
                stack.append(n)
            else:
                if not stack:
                    return False
                if n==")" and stack[-1]=="(" and stack:
                    stack.pop()
                elif n=="]" and stack[-1]=="[" and stack:
                    stack.pop()
                elif n=="}" and stack[-1]=="{" and stack:
                    stack.pop()
                else:
                    stack.append(n)
        if stack:
            return False
        return True
