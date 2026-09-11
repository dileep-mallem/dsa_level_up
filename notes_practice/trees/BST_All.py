# ALl op's of BST 

class Node :
    def __init__(self,val : int) : 
        self.val=val
        self.left=None 
        self.right=None

class BinarySearchTree : 
    def __init__(self) : 
        self.root=None 

 
    # Searching 
    def search(self,key : int) : 
        if self.root is None :
            return False
        temp=self.root 

        while temp : 
            if key==temp.val :
                return True
            elif key < temp.val :
                temp=temp.left 
            else :
                temp=temp.right 
        return False 

    # Insertion 
    def insertion(self,val) : 
        self.root = self.insertion_rec(self.root,val)

    def insertion_rec(self,node : Node , val : int) : 
        if node is None :
            return Node(val)

        if val < node.val :
            node.left=self.insertion_rec(node.left,val)
        elif val > node.val :
            node.right = self.insertion_rec(node.right,val)
        
        return node 

    # Inorder Traversal (Gets Sorted Values) 
    def inorder(self):
        result=[]
        def dfs(node) : 
            if node is None : 
                return 
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(self.root)
        return result

    # Find Min (Left Most) and max (right most)
    def find_min(self) : 
        if self.root is None :
            return 
        temp=self.root 
        while temp.left : 
            temp=temp.left 
        return temp.val

    def find_max(self) : 
        if self.root is None :
            return 
        temp=self.root 
        while temp.right : 
            temp=temp.right 
        return temp.val 

    # Height
    def height(self) : 
        def h(node) : 
            if node is None : 
                return -1 
            return 1 + max(h(node.left) ,h(node.right))
        return h(self.root)

tree=BinarySearchTree()

for i in [5,3,2,6,7,10,1,9,4,8] : 
    tree.insertion(i)

print("Inorder Travresal : ",tree.inorder())
h=tree.height()
minimum,maximum=tree.find_min(),tree.find_max()
print("Height of Tree : ",h)
print(f"Min : {minimum} Max : {maximum} ")
print(f"99 in Tree : {tree.search(99)}")


# Inorder Travresal :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Height of Tree :  5
# Min : 1 Max : 10 
# 99 in Tree : False
    


            