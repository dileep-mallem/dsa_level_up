# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # type: ignore
        def helper(left: int, right: int) -> TreeNode | None: # type: ignore
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid]) # type: ignore
            
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)