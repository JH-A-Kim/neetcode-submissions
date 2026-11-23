# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we have the head of a singly linked list. so we alternate the ordering between the value and then inbetween is the length - the iterating point. So a property is just that I must iterate through each point there is no way for me to get the index of the value. So first of all how do i know which value is the length - iterator? I need to keep track of it as i iterate. What ways can i do that? Maybe a list and then i create the indexes as i go? pointing to each value instead of the value. now how do i iterate through? also list can be up to 1000 this needs to be an O(n) solution. head will always be the same value. What if i just iterate through. Get each node associate it with an index in a list. and then iterate at each point check for that index and add the value as the new heads.next? 
        nodes = []

        node = head

        while node:
            nodes.append(node)
            node = node.next
        
        total = len(nodes)
        
        i, j = 0, total - 1

        while i<j:
            nodes[i].next = nodes[j]

            i+=1

            if i == j:
                break
            
            nodes[j].next = nodes[i]
            j-=1
        nodes[i].next = None

        