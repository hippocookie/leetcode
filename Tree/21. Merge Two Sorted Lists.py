from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_ptr = list1
        second_ptr = list2
        result = ListNode()
        tail = result

        while first_ptr is not None and second_ptr is not None:
            if first_ptr.val < second_ptr.val:
                tail.next = first_ptr
                first_ptr = first_ptr.next
            else:
                tail.next = second_ptr
                second_ptr = second_ptr.next
            tail = tail.next
        if first_ptr is not None:
            tail.next = first_ptr
        if second_ptr is not None:
            tail.next = second_ptr
        return result.next

if __name__ == '__main__':
    pass