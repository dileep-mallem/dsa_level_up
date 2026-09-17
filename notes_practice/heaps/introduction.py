# Why Heaps -> To reduce Time Complexity for Searching , Inserting or Deletion . 
# We can reduce sort for every Insertion and Can get min/max element(or for Given Condition) in O(n logn)tc and O(1) , resp using Arrays.
# but can reduce that Insertion Time using Heaps -> O(log n ) 

# heaps -> stored as an array but rep as tree
# Complete Binary Tree 
# Max Heap -> Parent >= Child 
# Min Heap -> Parent <=child 

# Node -> i, root=i=1
# parent[i] = i//2 
# left[i]=2*i
# right[i]=2*i+1
# NO pointers Needed  
# height = log(n)

# Insertion -> Up heap -> O(log n)
# Deletion -> O(log n)

class minHeap : 
    def __init__(self) : 
        self.heap=[]

    def parent(self,i) :
        return i//2 
    def left(self,i) :
        return 2*i
    def right(self,i) :
        return 2*i+1 

    def insert(self,val : int) :
        self.heap.append(val)
        self.shift_up(len(self.heap)-1)

    def shift_up(self,i) : 
        par=self.parent(i)

        if i>0 and self.heap[i] <self.heap[par] : 
            self.heap[i],self.heap[par]=self.heap[par],self.heap[i] # Swapping parent and Child 
            self.shift_up(par) # checking till Min Heap Condition Satisfies 

    def find_min(self) :
        return self.heap[0] if self.heap else None 

    # Extracting Min 
    def extract_min(self) :
        if len(self.heap)==0 :
            return None 
        if len(self.heap)==1 :
            return self.heap.pop()

        root=self.heap[0]

        # Move last Elemnt to Root and SHift it Down 
        self.heap[0]=self.heap.pop()
        self.shift_down(0)
        return root 
    def shift_down(self,i) :
        # Restores heap property downward after extraction
        left=self.left(i)
        right=self.right(i)
        smallest=i

        if left < len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right < len(self.heap) and self.heap[right]<self.heap[smallest]:
                    smallest=right 
        if smallest!=i :
             # Swap 
             self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i] 
             self.shift_down(smallest)

        

heap=minHeap()
for v in [5,7,9,8,11,12,14,13,10] : 
     heap.insert(v)
print("Heap : ",heap.heap)
print("Minimum element:", heap.find_min())         
print("Extracted minimum:", heap.extract_min()) 
print("New Heap : ",heap.heap)
print("New minimum element:", heap.find_min())





