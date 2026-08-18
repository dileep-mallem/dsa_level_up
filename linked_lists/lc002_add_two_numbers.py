# Time : O(m+n) Space : max(m,n) Optimsed 
# Heare we 3 loops Seprately but we can also write three loops in a single loops ( But same TC and SC , Just Stucture Change)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore

        result=None
        dummy=ListNode(0) # type: ignore
        head=dummy

        t1=l1 # head of first LL 
        t2=l2
        carry=0
        while t1 and t2 : 
            s=t1.val + t2.val 

            if carry!=0 :
                s+=carry
                carry=0
            current=s%10 

            if s > 9 :
                carry = s//10 

            newnode=ListNode(current) # type: ignore
            dummy.next=newnode 
            dummy=newnode

            t1=t1.next
            t2=t2.next  

        while t1 :
            s=t1.val 
            if carry!=0 :
                s+=carry
                carry=0
            current=s%10 

            if s > 9 :
                carry = s//10 

            newnode=ListNode(current) # type: ignore
            dummy.next=newnode
            dummy=newnode

            t1=t1.next 
        while t2 :
            s=t2.val 
            if carry!=0 :
                s+=carry
                carry=0
            current=s%10 

            if s > 9 :
                carry = s//10 

            newnode=ListNode(current) # type: ignore
            dummy.next=newnode
            dummy=newnode

            t2=t2.next
        
        if carry!=0 : 
            newnode=ListNode(carry) # type: ignore
            dummy.next=newnode 
            dummy=newnode 

        head=head.next 
        return  head

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0
        
#         # Single loop handles l1, l2, and the final carry
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
            
#             # Calculate sum and carry directly
#             total = val1 + val2 + carry
#             carry = total // 10
            
#             # Connect new node directly
#             current.next = ListNode(total % 10)
#             current = current.next
            
#             # Advance pointers safely
#             if l1: l1 = l1.next
#             if l2: l2 = l2.next
                
#         return dummy.next