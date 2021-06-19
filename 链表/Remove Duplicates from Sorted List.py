class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = head
        while p and p.next and p.val == p.next.val:
            tmp = p.next.next
            if p.next:
                p.next.next = None
            p.next = tmp
            if p.val != p.next.val:
                p = p.next 
        return head
