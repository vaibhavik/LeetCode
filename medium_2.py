'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


OPTIMAL SOLUTION ---

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ""
        b = ""
        c = []
        c1 =""
        while l1:
            a = a + str(l1.val)
            l1 = l1.next 

        while l2:
            b = b + str(l2.val)
            l2 = l2.next
        
        a = a[::-1]
        b = b[::-1]
        c1 = str(int(a) + int(b))
        for x in c1:
            c.append(int(x))
        
        n1 = c.pop()
        l = ListNode(n1)
        r = l
        while(len(c) != 0):
            n2 = c.pop()
            l.next = ListNode(n2)
            l = l.next
        return r
     