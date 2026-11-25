# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # given the head of a linked list and integer n remove the nth node from the end of the list and return the head. Ok so this just seems like i iterate to the nth node i save the previous node and the next node and simply point previous to next. this would be O(n) solution on what condition do we move the prev and the next. prev we should move when we confirm that the next value != n once the next value = n we do not move the prev. for nextN we move it forward always until the counter is = n i didnt read the problem correctly and did from front of list. Its actually n elements from the end of the list not including a zero index. So in this case we need to traverse the list to the end or we could theoretically take the list put it into a list with indexes and then simply cut out the index we dont need so 
        dummy = ListNode(0, head)
        right = head
        left = dummy

        while n>0:
            right = right.next
            n-=1
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
        





        