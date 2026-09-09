# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
        
        # Lets Traverse , and is Values are Mismatching  then Return False 
        
        r1,r2=deque(),deque()
        # INOrder -> root left right
        def dfs(node1,target_q) :
            if node1 is None : 
                target_q.append(None) 
                return
            target_q.append(node1.val)
            dfs(node1.left,target_q)
            dfs(node1.right,target_q)

        dfs(p,r1)
        dfs(q,r2)
        return r1==r2
