# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        if depth == 1:
            root = TreeNode(val, root)
        while queue:
            next_level=[]
            if level == depth - 2:
                for node in queue:
                    node.left = TreeNode(val, node.left, None)
                    node.right = TreeNode(val, None, node.right)
                break
            for node in queue:
                for child in [node.left, node.right]:
                    if child is not None: 
                        next_level.append(child)
            queue = next_level
            level+=1
        
        return root