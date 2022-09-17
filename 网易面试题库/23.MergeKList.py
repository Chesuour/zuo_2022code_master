import heapq
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergeKList(lists: List[ListNode]):
        heap = []
        for listi in lists:
            while listi:
                heapq.heappush(heap, listi.val)
                listi = listi.next

        dummy = ListNode(0)
        p = dummy
        while heap:
            p.next = ListNode(heapq.heappop(heap))
            p = p.next

        return dummy.next

if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    print(Solution.mergeKList(lists))