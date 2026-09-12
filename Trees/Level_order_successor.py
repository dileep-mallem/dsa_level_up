# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderSuccessor(self, root: Optional[TreeNode],key : int ) -> List[List[int]]: # type: ignore
        
        if not root:
            return None 
        
        result=None
        q=deque()
        q.append(root)

        while q :    
            currNode=q.popleft()   

            if currNode.left :
                q.append(currNode.left)
            if currNode.right :
                q.append(currNode.right)

            if currNode.val==key :
                return q[0] if q else None 
            
        return None



    
        
