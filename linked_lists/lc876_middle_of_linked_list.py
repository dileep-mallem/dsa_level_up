# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        # Brute : Find List size , tervrese to middle Time : O(n) + O(n//2) 

        # Optimal : Fast(moves two node) and Slow(moves One Node) Pointer

        slow = fast = head 

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next 
        return slow