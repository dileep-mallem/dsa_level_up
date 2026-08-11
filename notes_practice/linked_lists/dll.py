class Node : 
    def __init__(self,data : int) : 
        self.data=data 
        self.next=None 
        self.prev = None

class dll : 
    def __init__(self):
        self.head=None 
        self.tail= None # tail Pointer for O(1) ops


    def append(self,data) : 
        newnode=Node(data) 
        if not self.head  : 
            self.head=self.tail=newnode 
        else :
            newnode.prev=self.tail # newnode <- tail
            self.tail.next = newnode  # tail -> newnode 
            self.tail=newnode # update Tail 

    def prepend(self,data : int) : 
        newnode=Node(data)
        if not self.head : 
             self.head=self.tail=newnode
        else : 
            newnode.next=self.head # new node → old head
            self.head.prev=newnode # new node → old head
            self.head=newnode # Update Head

    def delete(self,value : int ):
        if self.head is None : 
            print("List is Empty")
            return 
        temp=self.head 
        curr=temp
        while temp:
            if temp.data == value :
                if temp.next :
                    temp.next.prev=curr
                else :                  # If temp.next is None (last Node)
                    self.tail=temp.prev # Tail to one back if Tail is Deleted 
                curr.next=temp.next
                print("Successfully Deleted")
                return
            curr=temp 
            temp=temp.next
        if temp is None : 
            print("Value Not Found")
            return
         
    def traverseBack(self) : # Unique to DLL 
    
        parts=[]
        temp=self.tail

        while temp :
            parts.append(str(temp.data))
            temp=temp.prev 
        return " <- ".join(parts)
    
    def __str__(self):
        parts, temp = [], self.head
        while temp:
            parts.append(str(temp.data)); 
            temp = temp.next
        return " ⇄ ".join(parts)
    
# Demo
dll = dll()
for v in [10, 20, 30]: dll.append(v)
dll.prepend(5)
print(dll)                        # 5 ⇄ 10 ⇄ 20 ⇄ 30
print(dll.traverseBack())    # 30 ← 20 ← 10 ← 5
dll.delete(20)
print(dll)                        # 5 ⇄ 10 ⇄ 30


# Real-world use: Python's collections.deque is implemented as a'
# ' doubly linked list internally — that's why appendleft() 
# and popleft() are O(1). Browser history (back/forward), undo/redo buffers,
# and music player queues are all DLL applications.
        
    
    

