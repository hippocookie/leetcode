from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev_node = None
        curt_node = head
        next_node = head.next
        while next_node:
            curt_node.next = prev_node
            prev_node = curt_node
            curt_node = next_node
            next_node = next_node.next
        curt_node.next = prev_node
        return curt_node
