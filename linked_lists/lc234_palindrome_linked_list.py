# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: # type: ignore
        # Fast path for empty or single node lists
        if not head or not head.next:
            return True

        # Find middle and then compare 
        def mid(head):
            slow=fast=head 
            while fast.next and fast.next.next :
                slow=slow.next 
                fast=fast.next.next 
            return slow 

        middle = mid(head)

        # Reverse Second half from mid (Except Mid)
        prev=middle
        curr=middle.next 

        while curr and curr.next : 
            nxt=curr.next 
            curr.next=nxt.next
            nxt.next=prev.next
            prev.next=nxt 

        # Now compare from head to middle and middle to last 
        t1=head 
        t2=middle.next # Starts after Middle 

        while t2 :
            if t1.val != t2.val :
                return False 
            t1=t1.next
            t2=t2.next 
        return True 
        

    #     class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # Fast path for empty or single node lists
    #     if not head or not head.next:
    #         return True
            
    #     rev = None
    #     slow = fast = head
        
    #     # Reverse the FIRST half while finding the middle
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         # Standard in-place linked list reversal
    #         nxt = slow.next
    #         slow.next = rev
    #         rev = slow
    #         slow = nxt
            
    #     # If the list has an odd number of elements, skip the center element
    #     if fast:
    #         slow = slow.next
            
    #     # Compare the reversed first half (rev) with the second half (slow)
    #     while rev and rev.val == slow.val:
    #         rev = rev.next
    #         slow = slow.next
            
    #     # If rev reached the end (None), it's a palindrome
    #     return not rev
