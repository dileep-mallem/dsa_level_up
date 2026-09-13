# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool: # type: ignore
        # xx,yy=findNode(x),findNode(y)

        
        
        def level(root , node : int ) :
            q=deque()
            q.append(root)
            result=1
            while q :
                n=len(q)

                for i in range(n):
                    curr=q.popleft()
                    # Check the node immediately when popped
                    if curr.val == node:
                        return result
                    if curr.left :
                        q.append(curr.left)
                    if curr.right :
                        q.append(curr.right)
                        
                result+=1

            return 0 
            
        def isSibling(root,node1 : int,node2 : int) :
            if root is None :
                return False
            if root.left and root.right : 
                if (root.left.val==node1 and root.right.val==node2) or (root.left.val==node2 and root.right.val==node1) :
                    return True 

            return isSibling(root.left,node1,node2) or isSibling(root.right,node1,node2)

        return ((level(root,x)==level(root,y)) and (not isSibling(root,x,y)))
            