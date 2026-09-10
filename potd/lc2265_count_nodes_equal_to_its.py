# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int: # type: ignore

        count_matching_st=0

        def dfs(node) : 
            nonlocal count_matching_st
            if not node :
                return 0,0 # current_sum,currrent_count 
            
            # Traverse tdown o left,right st's
            left_sum,left_count=dfs(node.left)
            right_sum,right_count=dfs(node.right)

            # CAluculate Values form Current Subtree 

            current_sum=node.val + left_sum + right_sum 
            current_count=1+left_count+right_count

            # 3. Check if the average equals the root's value (using integer division)
            if current_sum // current_count == node.val:
                count_matching_st+= 1

            # Pass the Data return to parent node 
            return current_sum,current_count

        dfs(root)
        return count_matching_st
