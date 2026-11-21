# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # has cycle i need to figure out if its a circular pointer system. This is relatively simple. I just need to follow 2 points. One moves at one speed the other at 2. If i reach None then there is no cycle if i ever reach the same node then we are have a cycle
        if not head:
            return False


        speed1, speed2 = head, head.next

        while speed1 and speed2:
            if speed1 == speed2:
                return True
            else:
                speed1 = speed1.next
                if speed2.next:
                    speed2 = speed2.next.next
                else:
                    return False
        return False
        