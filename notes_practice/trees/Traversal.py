# DFS -> Defth First Search

    # Pre Order -> node left right  , Used for evaluating a Amth Expression or making a copy , serilization of str/arr
    # Inorder -> left node right , we can visit nodes in Sorted Manner in BST 
    # post Order -> left right node 

# BFS -> Breadth First Search (Level by Level)

class Node : 
    def __init__(self,data : int) : 
        self.data=data 
        self.left=None 
        self.right=None 

# Insert Elements 

class BinaryTree : 
    def __init__(self) : 
        self.root=None

    def populate(self) : 
        value=int(input("Enter the Root Node Value : "))
        self.root=Node(value)
        self.populate_rec(self.root)

    def populate_rec(self,node) : 
        # Handles LEft Cild
        print(f"Do you want left of {node.data} :  ")
        left=bool(int(input()))

        if left : 
            value=int(input("Enter the  Node Value : "))
            node.left=Node(value)
            self.populate_rec(node.left)

        # Handles Right
        print(f"Do you want right of {node.data} :  ")
        right=bool(int(input()))
        if right : 
            value=int(input("Enter the  Node Value : "))
            node.right=Node(value)
            self.populate_rec(node.right) # Calling -> It will be on top of Stack 


    
    def display(self,node=None,level=0) : 
        if node is None and level==0 : 
            node=self.root
        if node is None : 
            return 
        # Display with clear visual indentation matching tree depth
        print("    " * level + f"└── {node.data}")
        
        self.display(node.left,level+1)
        self.display(node.right,level+1)

    def preOrder(self) : 
        result=[]

        def dfs(node) : 
            if not node : 
                return 
            result.append(node.data)
            dfs(node.left)
            dfs(node.right)
        dfs(self.root)

        return result
    
    def inOrder(self) : 
            result=[]
    
            def dfs(node) : 
                if not node : 
                    return 
                
                dfs(node.left)
                result.append(node.data)
                dfs(node.right)
            dfs(self.root)
    
            return result
    
    def postOrder(self) : 
                result=[]
        
                def dfs(node) : 
                    if not node : 
                        return 
                    
                    dfs(node.left)
                    dfs(node.right)
                    result.append(node.data)
                dfs(self.root)
        
                return result
    




# Execution 

tree=BinaryTree()
tree.populate()
print("\n--- Tree Stucture ---")
tree.display()

print("\n--Pre Order --")
print(tree.preOrder())

print("\n--In Order")
print(tree.inOrder())

print("\n--Post Order")
print(tree.postOrder())