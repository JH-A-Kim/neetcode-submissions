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

        while list1 and list2: # here i go until one i have reached the endpoint. I then set the current values next to be the current valid value which is just the smallest number val. and then i move that list forward. and then i move the list forward. Eventually if there exists more of a list at the end then we simply just add that list to the next part of the node and we dont have to do anything more. then we return our placeholder node.next as the head. 
            if list1.val <= list2.val:
                newList.next = list1 # here we are pre setting the next value so we are always ending at the last part of the list and we are never at newList = None 
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
            newList = newList.next

        newList.next = list1 or list2

        return placeholder.next

        
        

        