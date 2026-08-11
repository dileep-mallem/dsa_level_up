# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        # Travese and Find LL length and remove (lenght-n+1) from Front 

        curr = head 
        l=0
        while curr : # O(n)
            l+=1
            curr=curr.next 
        
        pos = l - n + 1
        if pos == 1 : 
            head = head.next 
            return head
        temp=head 
        prev=temp
        for i in range(pos-1) :
            prev=temp
            temp=temp.next 

        prev.next = temp.next 

        return head 