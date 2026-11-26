"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # given the head of a linked list. each node has a pointer called random which can point to any node in the list or null. We must create a deep copy of the list. return the head of the copied linked list. Is this just not iterating through and then just making a copy of everything. I guess it needs to point to the new stuff and not the old so the next will be fine but the random is not. How do i get the random values and point them appropriately. I can potentially use a placeholder value? No in a rudimentary approach i can do 2 pass throughs. meaning O(n) time but on my second pass through how am i saving the value or i can use a hash table of placements. But on what parameters? and what keys? This would need the old node as the key and the new node as the value so that after the first pass through each node exists. and then we can just tie everything together because for the .next values its always just the next value where as for the random we just use the random value and it points to the correct node. node as a key and since a .random and .next point to a node those can be used as they can always point to that value that represent their random and after making each node individually I have something to point to using the original nodes from the given head. 
        curr_to_old = {None:None}

        curr = head

        while curr:
            curr_to_old[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            clone = curr_to_old[curr]
            clone.next = curr_to_old[curr.next]
            clone.random = curr_to_old[curr.random]
            curr = curr.next
        
        return curr_to_old[head]
        
        

        