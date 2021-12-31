# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #DFS
        def getLargestBranchDiff(node, vals):
            if node is None:
                return abs(max(vals) - min(vals))
            vals.append(node.val)
            ans = max(getLargestBranchDiff(node.left, vals), getLargestBranchDiff(node.right, vals))
            del vals[-1]
            return ans
        return getLargestBranchDiff(root, [])
        
        