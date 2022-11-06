from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None

if __name__ == '__main__':
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    Solution().detectCycle(n1)
