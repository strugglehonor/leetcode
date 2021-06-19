class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = p = ListNode(-120, head)
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                x = p.next.val
                while p.next and x == p.next.val:
                    p.next = p.next.next
            else:
                p = p.next
        return dummy.next
