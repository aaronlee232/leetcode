# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Start from leaves, invert, backtrack, invert, etc
        return self.recInvert(root)
        return self.iterInvert(root)


    def recInvert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None 

        left = self.recInvert(root.left)
        right = self.recInvert(root.right)

        root.left = right
        root.right = left

        return root


    def iterInvert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while len(stack) > 0:
            cur = stack.pop()

            origLeft = cur.left
            origRight = cur.right
            cur.left = origRight
            cur.right = origLeft

            if cur is not None:
                stack.append(cur.left)   
                stack.append(cur.right)
