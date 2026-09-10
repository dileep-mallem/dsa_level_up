# BST -> For every root , the values of its left Subtree should be Smaller and VAluef of Its right Subtree is greater 


class Node : 
    def __init__(self,val : int) : 
        self.val=val
        self.left=None
        self.right=None

    def __repr__(self):
        return f"Treeroot {self.data}"
    
class BinarySearchTree :

    def __init__(self) : 
        self.root=None 

    def insert(self,val) : 
        self.root=self.insert_rec(self.root,val)

    def insert_rec(self,root : Node ,val : int) : 
        if root is None: 
            return Node(val)

        if val < root.val : 
            root.left=self.insert_rec(root.left,val)
        elif val > root.val :
            root.right=self.insert_rec(root.right,val)

        return root
    
    def inorder(self):
        """Public method for Inorder Traversal (Prints sorted values)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.val)
            self._inorder_recursive(root.right, result)
    

if __name__=="__main__" :
    bst=BinarySearchTree()

    # Insert Elemnts 
    elements = [50, 30, 20, 40, 70, 60, 80]
    for v in elements : 
        bst.insert(v)

    print("Inorder traversal (Sorted):", bst.inorder()) 
    # Output: [20, 30, 40, 50, 60, 70, 80]