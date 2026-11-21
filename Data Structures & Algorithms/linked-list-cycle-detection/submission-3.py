# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # has cycle i need to figure out if its a circular pointer system. This is relatively simple. I just need to follow 2 points. One moves at one speed the other at 2. If i reach None then there is no cycle if i ever reach the same node then we are have a cycle

        speed1, speed2 = head, head

        while speed2 and speed2.next:
            speed1 = speed1.next
            speed2 = speed2.next.next
            if speed1 == speed2:
                return True
        return False
        