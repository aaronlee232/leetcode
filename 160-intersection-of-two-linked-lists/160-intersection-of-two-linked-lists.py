# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # maps node to the number of references to that node. earliest node with 2 references is the interesection node
        nodes = {}
        a = headA
        while a:
            nodes[a] = 1
            a = a.next
            
        b = headB
        while b:
            nodes[b] = nodes.get(b, 0) + 1
            if nodes[b] == 2:
                return b
            b = b.next
        
        return None