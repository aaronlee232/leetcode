# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        temp = []
        depth = 0
        
        if not root:
            return 0
        
        while queue:
            node = queue.pop()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            # replace queue with new row when entire row is checked
            if not queue:
                queue = temp
                temp = []
                depth+=1
        return depth

            
                
            