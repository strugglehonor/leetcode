class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        former = ListNode()
        dummy = last = ListNode()
        former.next = head
        last.next = head
        for i in range(n):
            former = former.next
        while former != None and former.next != None:
            last = last.next
            former = former.next
        last.next = last.next.next if last.next else None
        return dummy.next
