# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMiddleIndex() -> int:
            size = 0
            temp = head
            while temp != None:
                size += 1
                temp = temp.next
            return size//2
        mid = getMiddleIndex()
        
        if mid == 0:
            return None
        
        midNode: ListNode = head
        midNodePrev: ListNode = head
        i = 0
        while i != mid:
            midNodePrev = midNode
            midNode = midNode.next
            i += 1
        midNodePrev.next = midNode.next
        return head