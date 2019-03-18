class Solution(object):
    def isValid(self, strs):
        s =[]
        accept = {
		    '(':')',
		    '{':'}',
		    '[':']'}
        top=""	
        for i in range(0,len(strs)):
            s.append(strs[i])
            if strs[i] == accept.get(top):
                s.pop()
                s.pop()
                if len(s) >0:
                    top = s[len(s)-1]
            else:
                top = strs[i]
                print top
        if len(s) == 0:
            return True
        else:
            return False

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

'''