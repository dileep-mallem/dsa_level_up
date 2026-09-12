# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        if not root :
            return []
        
        zig=0 # 0 left , 1 right 
        q=deque()
        result=[]

        q.append(root)

        while q :
            n=len(q)
            l=[]
            for i in range(n):
                curr_node=q.popleft()
                l.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right :
                    q.append(curr_node.right)
            result.append(l)
            # if zig==0 : # Time : O(m) but space takes More ,
            #     result.append(l)
            #     zig=1
            # elif zig==1 :
            #     l=l[::-1]
            #     result.append(l)
            #     zig=0

        for i in range(len(result)) : # O(n)
            if i%2==1 :
                result[i].reverse()  # Time :O(m)  but Space ; O(1)

        return result

# Overall Time :O(n) Space : O(n)