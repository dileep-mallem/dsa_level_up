# BST -> For every Node , the values of its left Subtree should be Smaller and VAluef of Its right Subtree is greater 

class Node : 
    def __init__(self,val) : 
        self.data=val
        self.left=None
        self.right=None
        self.height=0

    def getData(self) : 
        return self.data

class BinarySearchTree : 
    def __init__(self) : 
        self.root=None 

    def heightNode(self,node : Node) : 
        if node is None : 
            return -1 
        return node.height

    def isEmpty(self) :
        return self.root is None 

    def display(self,node : Node,details : str) :
        if node is None :
            return
        print(f"{details}{node.getData()}")
        if node.left:
            self.display(node.left, f"Left child of {node.getData()} : ")
        if node.right:
            self.display(node.right, f"Right child of {node.getData()} : ")
        
    def insertion(self,val):
        def insert(node :Node,val : int) : 
            if node is None :
                return Node(val)
            
            if val < node.data : 
                node.left=insert(node.left,val)
            elif val > node.data : 
                node.right=insert(node.right,val)

            node.height=max(self.heightNode(node.left),self.heightNode(node.right)) + 1

            return node
        self.root = insert(self.root,val)
        

    def preOrder(self): 
        result=[]

        def dfs(node) : 
            if not node : 
                return 
            result.append(node.data)
            dfs(node.left)
            dfs(node.right)
        dfs(self.root)
        return result 

tree=BinarySearchTree()
arr=[15,10,20,5,12,8]

for i in arr : 
    tree.insertion(i)
print("Pre-order Traversal:", tree.preOrder())
print("\nTree Structure:")
tree.display(tree.root, "Root: ")

    
    