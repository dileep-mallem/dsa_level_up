# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]: # type: ignore
        
        if not root:
            return []

        result=[]
        q=deque()

        q.append(root)

        while q :
            n=len(q)
            
            avg_level=0
           
            for i in range(n) : 
                curr_node=q.popleft()
                avg_level+=curr_node.val
                if curr_node.left :
                    q.append(curr_node.left)
                if curr_node.right :
                    q.append(curr_node.right)

            avg=avg_level/n

            result.append(avg)
        return result
