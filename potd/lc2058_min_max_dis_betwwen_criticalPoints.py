# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]: # type: ignore 

        if not head or head.next is None or head.next.next is None :
            return [-1,-1]

        prev=head
        curr=head.next
        next=curr.next 
        critical_indices=[]
        index=1
        while next :
            if prev.val > curr.val < next.val : # min crital Point
                critical_indices.append(index)
            elif prev.val < curr.val > next.val : # max critical Point 
                critical_indices.append(index)
            index+=1 
            prev=prev.next
            curr=curr.next
            next=next.next

        # If there are fewer than 2 critical points, we can't calculate distances
        if len(critical_indices) < 2:
            return [-1, -1]

         # Maximum distance is always between the first and last critical point
        max_dist = critical_indices[-1] - critical_indices[0]

        #min_dis , chweck evry Possibity betwwen Two Indeices 
        min_dist = float('inf')
        for i in range(1, len(critical_indices)):
            min_dist = min(min_dist, critical_indices[i] - critical_indices[i - 1])

        return [min_dist,max_dist]