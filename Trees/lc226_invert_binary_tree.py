# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
        # Post Order : Swap left -> right ->  node 
        def postorder(node) : 
            if node is None :
                return None
            left=postorder(node.left)
            right=postorder(node.right)

            node.left,node.right=right,left
            return node 

        

        return postorder(root)