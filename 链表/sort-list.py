class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
           return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        nxt = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(nxt)
        # sort two ListNode
        dummy = p = ListNode(0)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            # p指针往后移动，容易漏
            p = p.next
        p.next = left if left else right
        return dummy.next
