'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# HINT :  Use a dummy list and append smallest node to it. 
#(initialised dummy with 0 and removed it before returning)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = l1
        h2 = l2
        i=0
        d = ListNode(0)
        tail = d
        while(h1 or h2):

            if h1 is None and h2 is not None:
                a  = ListNode(h2.val)
                h2 = h2.next
            
            elif h2 is None and h1 is not None:
                a = ListNode(h1.val)
                h1 = h1.next 
                
            elif h1.val >= h2.val:
                a = ListNode(h2.val)
                h2 = h2.next
                
            elif h1.val < h2.val:
                a = ListNode(h1.val)
                h1 = h1.next 
                
            tail.next = a
            tail = a
            
        curr = d
        d = curr.next
        curr.next = None
        
        return d