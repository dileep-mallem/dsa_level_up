from collections import deque
class Node : 
    def __init__(self,val) : 
        self.val=val 
        self.left=None 
        self.right=None 

class BinaryTree : 
    def __init__(self,val) : 
        self.root=Node(val) 

    # def insert(self,val) : 
    #     self.root=self.insert_rec(self.root,val) 

    # def insert_rec(self,node : Node , val : int) : 
    #     if node is None : 
    #         return Node(val)

    #     if val < node.val : 
    #         node.left=self.insert_rec(node.left,val) 
    #     elif val > node.val :
    #         node.right=self.insert_rec(node.right,val)

    #     return node 

    def inorder(self) :
        result=[]
        def dfs(node) : 
            if node is None : 
                return
            
            dfs(node.left) 
            result.append(node.val)
            dfs(node.right)
        dfs(self.root)
        return result
    # BFS (Time : O(n) Space : O(n/2) -> O(n))

    def search(self) : 
        result=[]

        def bfs(node) : 
            if node is None : 
                return 
            result.append(node.val) # [3,9,20,15,7]
            bfs(node.left)
            bfs(node.right)
        bfs(self.root)

        return result
    # For List of Lists of Child 
    def levelOrder(self, root):
        
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

        return result


    


bst=BinaryTree(3)

bst.root.left=Node(9)
bst.root.right=Node(20)
bst.root.right.left=Node(15)
bst.root.right.right=Node(7)


print(bst.inorder()) # [9, 3, 15, 20, 7]
print(bst.search()) # [3, 9, 20, 15, 7]
print(bst.levelOrder(bst.root)) # [[3], [9, 20], [15, 7]]

       
     

        
     

        