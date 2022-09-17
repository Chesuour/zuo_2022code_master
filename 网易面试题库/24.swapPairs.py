from typing import Optional, Callable, Any, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs( head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy

        while temp.next and temp.next.next :
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1

            temp = node1

        return dummy.next

if __name__ == "__main__":
    head = [1,2,3,4]
    print(Solution.swapPairs(head))