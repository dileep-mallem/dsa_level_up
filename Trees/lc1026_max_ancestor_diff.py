# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int: # type: ignore
        if not root :
            return 0 
        def preorder(node,max_val,min_val) :
            if not node :
                return abs(max_val-min_val)

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            

            left=preorder(node.left,max_val,min_val)
            right=preorder(node.right,max_val,min_val)

            return max(left,right)
        return preorder(root, root.val, root.val)
