# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ok so when we are merging 2 sorted lists i just take the value from the list that is less than the other add and move forward. Problems I need to save the head. And i cant go next on a none value. Where can i take this?

        placeholder = ListNode()

        newList = placeholder

        while list1 and list2:
            if list1.val <= list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
            newList = newList.next

        newList.next = list1 or list2

        return placeholder.next

        
        

        