class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        while not head:return head
        former, last = head, head
        for i in range(k):
            former = former.next
        while former != None:
            former = former.next
            last = last.next
        return last
