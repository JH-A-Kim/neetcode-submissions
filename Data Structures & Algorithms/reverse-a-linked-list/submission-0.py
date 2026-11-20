# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse linked list so I am given the head of a linked list and i need to reverse it this implementation should be O(n) or faster. So by its property I could take it one step at a time. I start at the head and initialize it as a node. that goes to null i go to the next value and then i set that values next as the previous node and then continue on and then return the last value as a head. 
        prev = None
        curr = head
        while curr:
            temp = curr.next # we save the next step node
            curr.next = prev # flip the pointer to point to the previous node
            prev = curr # move the prev pointer forward to the current that we are at
            curr = temp # move the curr forward eventually we land on curr = None and prev equal the new head
        return prev
        