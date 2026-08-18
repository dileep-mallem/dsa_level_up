# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. Using Stack (Time : O(2n) and Space : O(n))
# temp=head
# stack=[]
# while temp :
#     stack.append(temp.data)
#     temp=temp.next
# temp=head 
# while temp :
#     temp.data=stack.pop()
#     temp=temp.data


# 2 . Reversing the Links of Each Ny storing NExt next node first , then changing Link to prev , and prev pointer Incertmet and cuurnt pointer increments to next 
#  1 -> 2 -> 3 -> None( 1 head )
# None <- 1 <- 2 <- 3 ( 3 head (prev Node(as Cuur node turns None at last) ))



# Iterative : O(n) dpace : O(1
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        prev = None  
        curr = head 

        while curr : 
            next = curr.next # Stores NExt Node 
            curr.next = prev #(Pointing before Data)
            prev = curr 
            curr =next 
        return prev

# Recursive Approach

def reverse(head) : 
    if head is None or head.next is None :
        return head
    
    # Recurse: reverse everything after head   
    newHead = reverse(head.next)
    # head.next is now the last node of the reversed sublist
    # Make it point BACK to head
    front = head.next
    front.next=head  
    # Can also write above two as head.next.next=head
    head.next=None 

    return newHead 



