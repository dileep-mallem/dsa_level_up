# AVL is a Self Balancing BST, where Balance factores of each ndoe is 0 ,1,-1
# It solved the Searching, other Things of BSt where it can go to the Wort TC , so AVl happend , to Reduce TC 


# time Complexities : 
    # Insertion : log(n) + O(1)-> roatation(max two rotations) -> O(logn)
    # Searching : O(logn)
    # Deletion : O(log n)
    # rotations :O(1)

# Balance Factor = height(left subtree) - height(right subtree)


class Node : 
    def __init__(self,val) : 
        self.key=val 
        self.left=None 
        self.right=None 
        self.height=1 

class AVL : 
    def __init__(self) : 
        self.root=None 

    def get_height(self,node) : 
        if node is None: 
            return 0
        return node.height

    def get_balance(self,node) : 
        if node is None :
            return 0 
        return (self.get_height(node.left)-self.get_height(node.right))

    def update_height(self,node) : 
        node.height=1+max(
            self.get_height(node.left),
            self.get_height(node.right)
        )
     # ---------- Rotations ----------

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self.update_height(z)
        self.update_height(y)

        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y
    
    # ---------- Insert ----------

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # Normal BST insertion
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)

        elif key > node.key:
            node.right = self._insert(node.right, key)

        else:
            # Ignore duplicate
            return node

        # Update height
        self.update_height(node)

        # Check balance
        balance = self.get_balance(node)

        # LL
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # RR
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # LR
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RL
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result) 

tree=AVL()

for v in [30,20,10] : 
    tree.insert(v)

print(tree.inorder())     # [10, 20, 30]