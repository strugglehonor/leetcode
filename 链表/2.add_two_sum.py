class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        # 进位
        add = 0
        # 数字位 
        num = 0
        # 结果为返回dummy.next
        dummy = resNode = ListNode()
        while p or q:
            n = p.val if p else 0
            m = q.val if q else 0
            num = (m+n+add)%10
            add = (m+n+add)//10
            resNode.next = ListNode(num)
            resNode = resNode.next
            # 进行
            if p:p = p.next
            if q:q = q.next
        # 如果还有进位，需要加到末尾
        if add != 0:
            resNode.next = ListNode(add)
        # 注意resNode.next才是第一个节点
        return dummy.next
