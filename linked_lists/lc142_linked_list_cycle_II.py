# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        if not head or not head.next:
            return None
        # Fast and Slow pointer Algo 

        fast=slow=head 

        while fast and fast.next : 
            slow=slow.next 
            fast=fast.next.next 

            if slow is fast : # Cycle Detected 
                slow2=head 
                # i=0
                while slow is not slow2 : # is is faster tehn ==
                    slow2=slow2.next
                    slow=slow.next 
                    # i+=1 if to return index where Cycle begins 

                return slow  # return i
        return None # If fast or fast.next become None , No cycel , so -1