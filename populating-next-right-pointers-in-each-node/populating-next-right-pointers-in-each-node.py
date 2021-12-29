"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # tree is empty
        if root is None:
            return
        
        queue = [root]
        while queue:
            cur = queue.pop(0)
            hasChildren = cur.left is not None and cur.right is not None
            
            # set next of left node to its right node
            if hasChildren:
                cur.left.next = cur.right
                
                # set next of right node to its right node
                if cur.next:
                    cur.right.next = cur.next.left
                
                # if children are not null, add to queue (continue condition)
                queue.append(cur.left)
                queue.append(cur.right)
        return root