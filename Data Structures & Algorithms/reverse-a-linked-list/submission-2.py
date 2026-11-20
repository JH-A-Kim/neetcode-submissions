# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse linked list so I am given the head of a linked list and i need to reverse it this implementation should be O(n) or faster. So by its property I could take it one step at a time. I start at the head and initialize it as a node. that goes to null i go to the next value and then i set that values next as the previous node and then continue on and then return the last value as a head. 
        # we save the next step node
          # flip the pointer to point to the previous node
       # move the prev pointer forward to the current that we are at
        # move the curr forward eventually we land on curr = None and prev equal the new head


        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
        # think of it like effectively breaking off a section one by one like lego and then connecting it the other way as we go. so it might be like red blue green but i break off green and then i break off blue connect and then same with red giving me green blue red. I save the next value i set the current values next to the previous value we saved and then i move forward.

        