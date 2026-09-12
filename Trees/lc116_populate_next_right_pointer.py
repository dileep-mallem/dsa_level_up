"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]': # type: ignore
        if not root:
            return None
        
        q=deque()
        q.append(root)
    
        while q :
            n=len(q)
            
            for i in range(n) : 
                currNode=q.popleft()
                
                
                if i<n-1 :
                    currNode.next = q[0]
                if i==n-1 :
                    currNode.next=None
                if currNode.left :
                    q.append(currNode.left)
                if currNode.right :
                    q.append(currNode.right)

        return root