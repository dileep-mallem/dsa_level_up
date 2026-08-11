# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        prev = None 
        curr = head 

        while curr : 
            next = curr.next # Stores NExt Node 
            curr.next = prev #(Pointing before Data)
            prev = curr 
            curr =next 
        return prev