# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head):
        p = head
        a = []
        while p!=None:
            a.insert(0, p.val)
            p = p.next
        return a