# https://leetcode-cn.com/problems/palindrome-linked-list/
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        array = []
        p = head
        while p:
            array.append(p.val)
            p = p.next
        return array == array[::-1]
