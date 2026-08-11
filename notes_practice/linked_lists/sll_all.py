class Node : 
    def __init__(self,data : int ) : 
        self.data=data 
        self.next=None 

class LinkedList : 

    def __init__(self) : 
        self.head=None

    # Display
    def display(self) :
        if self.head is None : 
            print("Linked List is Empty")
            return
        temp=self.head 
        while temp : 
            print(temp.data,end=" ")
            temp=temp.next 
        print()
    # Insertion 
    def insert(self,value) : 
        newnode=Node(value)
        if self.head is None :  
            self.head=newnode 
            return

        #traverse to the last 
        temp=self.head 
        while temp.next!=None : 
            temp=temp.next 
        temp.next=newnode 

    # Insertion at Specif Postion 
    def insert_pos(self,value : int,pos : int ) :
        newnode=Node(value) 

        if pos==1 :
            newnode.next=self.head 
            self.head=newnode 
            return 
        temp=self.head 
        for i in range(1,pos-1) : 
            temp=temp.next 
        if temp is None : 
            print("Position out of Bounds")
            return

        newnode.next=temp.next 
        temp.next=newnode 

    # Delete a Value 
    def delete_val(self,value : int ) :
        if not self.head:
            print("List is empty")
            return
        if self.head.data==value : 
            self.head=self.head.next
            return 
        temp=self.head 
        while temp.next : 
            if temp.next.data==value : 
                temp.next=temp.next.next
                return 
            temp=temp.next

        print("Value is Not Present")
        
                   
    # Deletion at Specific Position 

    def delete_pos(self,pos) : 
        if not self.head:
                print("List is empty")
                return
        if pos < 1:
            print("Invalid Position!")
            return
        if pos==1 :
            self.head=self.head.next 
            return
        
        temp=self.head
        for i in range(1,pos-1) : 
            if temp is None or temp.next is None:
                print("Position out of bounds!")
                return
            temp=temp.next 
        if temp is None or temp.next is None:
                print("Position out of bounds!")
                return
        temp.next=temp.next.next

l=LinkedList()

while True : 
    print("-- 1.Insert 2.Insert by pos 3.Delete by pos 4.Delete by Value 5 Display 6.Exit --")
    choice = int(input("Enter Choice : "))

    match choice : 
        case 1 :
            x=int(input("Enter Value : "))
            l.insert(x)
        case 2 : 
            x=int(input("Enter Value : "))
            pos=int(input("Enter Position : "))
            l.insert_pos(x,pos)
        case 3 : 
            pos=int(input("Enter Position : "))
            l.delete_pos(pos)
        case 4 : 
            x=int(input("Enter Value : "))
            l.delete_val(x)
        case 5 :
            l.display()
        case 6 :
            break
        case _:
            print("Enter Correct Choice ")







