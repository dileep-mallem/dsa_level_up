# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # type: ignore
        if root is None :
            return True
        q=deque()
        q.append(root)
        
        while q :
            n=len(q)
            l=[]
            for i in range(n):
                curr=q.popleft()
                if curr :
                    l.append(curr.val)
                    q.append(curr.left) # Append even If they are None
                    q.append(curr.right)
                else :
                    l.append(None) # Store absence of node Explicit

            if l!=l[::-1]: # not .reverse() -> It Modifies
                return False   

        return True 
