# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        if not root:
            return []
        result=[]
        q=deque()
        q.append(root)

        while q :
            n=len(q)
            currList=[]
            for i in range(n) : 
                currNode=q.popleft()
                currList.append(currNode.val)

                if currNode.left :
                    q.append(currNode.left)
                if currNode.right :
                    q.append(currNode.right)
                
            result.append(currList)

        return result[::-1]