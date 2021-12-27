# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        dummy = ListNode()
        
        # case 1 both list nodes are not None
        # add l1 l2 and carry
        # output ones digit to sum node
        # output tens digit in carry
        temp = dummy
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            val %= 10
            temp.next = ListNode(val, None)
            l1, l2, temp = l1.next, l2.next, temp.next
        
        # case 2 one list node is None
        # add non None list node with carry
        # output ones digit to sum
        # output tens digit in carry
        leftOver = l1 if l1 is not None else l2
        while leftOver:
            val = leftOver.val + carry
            carry = val // 10
            val %= 10
            temp.next = ListNode(val, None)
            leftOver, temp = leftOver.next, temp.next
            
        # case 3 both list nodes are None
        # if carry not zero output to sum
        # end loop
        if carry:
           temp.next = ListNode(carry, None) 
        return dummy.next
        