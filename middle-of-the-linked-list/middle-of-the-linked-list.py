# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stored = []
        size = 0
        temp = head
        while temp:
            size += 1
            stored.append(temp)
            temp = temp.next
        return stored[size//2]