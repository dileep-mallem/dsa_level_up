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


# Execution 

tree=BinaryTree()
tree.populate()
print("\n--- Tree Stucture ---")
tree.display()




    
        



