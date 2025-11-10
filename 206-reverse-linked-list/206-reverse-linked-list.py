# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.iterReverse(head)
        # return self.betterIterReverse(head)

        cur = head
        if cur is None:
            return None

        while cur.next is not None:
            cur = cur.next
        
        new_head = cur

        self.betterRecReverse(head)
        return new_head 
    
    def iterReverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        # reversing = stack
        val_stack = []
        cur = head
        while cur is not None:
            val_stack.append(cur.val)
            cur = cur.next
        
        print(val_stack)

        new_head = ListNode(val_stack.pop(), None)
        cur = new_head
        while len(val_stack) > 0:
            cur.next = ListNode(val_stack.pop(), None)
            cur = cur.next

        return new_head

    def betterIterReverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur

            cur = next_node
        
        return prev


    def betterRecReverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://stackoverflow.com/questions/354875/reversing-a-linked-list-in-java-recursively
        if (head.next is None):
            return head

        next_node = head.next
        head.next = None  # prevent cycle
         
        prev = self.betterRecReverse(next_node)
        prev.next = head
        return head