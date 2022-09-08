# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        trail = None
        while temp:
            if trail and trail.val == temp.val:
                trail.next = temp.next
                temp = temp.next
            else:
                trail = temp
                temp = temp.next
                
        return head