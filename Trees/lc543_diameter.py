# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        diameter=0

        def height(node) : 
            nonlocal diameter
            if node is None :
                return -1 
            left=height(node.left)
            right=height(node.right)

            dia = left + right +2
            diameter = max(diameter,dia)
            return 1 + max(left,right)

        height(root)

        return diameter