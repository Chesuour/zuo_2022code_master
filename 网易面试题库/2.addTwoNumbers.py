from typing import Optional, Callable, Any, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = pre = ListNode()
        add = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y
            cur.next = ListNode(total%10)
            cur = cur.next
            add = total // 10

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        if add : cur.next = ListNode(add)
        return pre.next

if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    print(Solution.addTwoNumbers(l1, l2))