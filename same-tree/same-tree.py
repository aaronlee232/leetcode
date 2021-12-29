# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        
        pQueue = deque([p])
        qQueue = deque([q])
        while pQueue and qQueue:
            pCur = pQueue.popleft()
            qCur = qQueue.popleft()
            
            if bool(pCur.left) != bool(qCur.left) or bool(pCur.right) != bool(qCur.right):
                return False
            
            if pCur.val != qCur.val:
                return False
            
            
            if pCur.left:
                pQueue.append(pCur.left)
                qQueue.append(qCur.left)
            if pCur.right:
                pQueue.append(pCur.right)
                qQueue.append(qCur.right)
            
        return len(pQueue) == len(qQueue) == 0