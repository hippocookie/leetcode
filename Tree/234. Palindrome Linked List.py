from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        length = 0
        curt = head
        while curt:
            length += 1
            curt = curt.next
        if length % 2 == 1:
            return False
        prev = None
        curt = head
        fast = head.next
        for i in range(length // 2):
            curt.next = prev
            prev = curt
            curt = fast
            fast = fast.next
        while curt and fast:
            if curt.val != fast.val:
               return False
        return True

if __name__ == '__main__':
    n1 = ListNode(0)
    n2 = ListNode(1)
    n1.next = n2
    print(Solution().isPalindrome(n1))