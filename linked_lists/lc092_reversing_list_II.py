# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]: # type: ignore # type : ignore
        if not head or left == right:
            return head

        # Create new list with dummy and head 
        dummy = ListNode(0) # type: ignore
        dummy.next=head
        pre=dummy

        for _ in range(left-1) : 
            pre=pre.next
            
        cur = pre.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
            
        return dummy.next