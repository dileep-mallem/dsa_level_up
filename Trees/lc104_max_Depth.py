# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        # Base case: if the node is empty, the depth is 0
        if not root:
            return 0

        # Recursively find the depth of both subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the current node is 1 plus the maximum of its subtrees
        return 1 + max(left_depth, right_depth)