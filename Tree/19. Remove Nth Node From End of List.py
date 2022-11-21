from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast_cursor = dummy
        slow_cursor = dummy
        for i in range(n):
            fast_cursor = fast_cursor.next
        while fast_cursor.next:
            slow_cursor = slow_cursor.next
            fast_cursor = fast_cursor.next

        slow_cursor.next = slow_cursor.next.next
        return dummy.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    result= (Solution().removeNthFromEnd(n1, 1))
    print(result)

