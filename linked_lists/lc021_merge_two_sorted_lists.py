# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        

        dummy = ListNode(0) # type: ignore
        head = dummy

        temp1=list1 
        temp2=list2 

        while temp1 and temp2 :
            if temp1.val <= temp2.val :
                newnode=ListNode(temp1.val) # type: ignore
                temp1=temp1.next 
                dummy.next=newnode 
                dummy =newnode 
            elif temp2.val <= temp1.val :
                newnode=ListNode(temp2.val) # type: ignore
                temp2=temp2.next 
            
                dummy.next=newnode 
                dummy =newnode 
        
        while temp1 :
            newnode=ListNode(temp1.val) # type: ignore
            dummy.next=newnode 
            dummy =newnode
            temp1=temp1.next 
        while temp2 :
            newnode=ListNode(temp2.val) # type: ignore
            dummy.next=newnode 
            dummy =newnode
            temp2=temp2.next 

        # Remove head (Dummy) and Return 
        head=head.next 

        return head 
        