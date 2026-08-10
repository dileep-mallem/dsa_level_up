# Linked Lists is in HEp , Head var in stack pintd to First NOde in Heap 

# 3 -> 4 -> 5 -> 1

# Every Node ha Data and Address of next node s

class Node : 

    def __init__(self,value : int) : 
        self.data = value
        self.next=None 

class LL : 
    def __init__(self) :
        self.head=None

    def display(self) : 
        if self.head is None : 
            print("Empty Linked List \n")
        temp = self.head 

        while temp : 
            print(temp.data , "->",end="")
            temp=temp.next
        print()

    def insert_at_beginning(self,value) : 
        newnode = Node(value) 
        newnode.next=self.head

        self.head=newnode
    def insert_at_end(self,data) : 
        newnode=Node(data) 

        if self.head is None:
            self.head = newnode
            return

        temp=self.head 
        while temp.next : 
            temp=temp.next 

        temp.next=newnode

    def delete_value(self,value) : 
        if self.head is None : 
            return "Linked List is Empty" 
        
        temp=self.head 

        # If value is in First Node(head)
        if self.head.data==value : 
            self.head=self.head.next

        # Else
        while temp.next and temp.next.data!=value : 
            temp=temp.next
        if temp.next : 
            temp.next=temp.next.next 
            print("Updated Linked List : ",end="")
            self.display()
        if temp.next is None: 
            print("No Value")

l=LL()

l.display()
l.insert_at_beginning(10)
l.insert_at_end(20)
l.insert_at_end(30)
l.insert_at_beginning(0)
l.display()
l.delete_value(10)
l.delete_value(90)



   
        

             
        
    


        




