# tail's pointer connects to head 
# we can detect by curr.next=head , NO None terminator 

class Node :
    def __init__(self,val:int): 
        self.data=val 
        self.next=None 
class cll :
    def __init__(self) : 
        self.head=None 

    def append(self,val : int ) : 
        newnode=Node(val) 

        if not self.head : 
            self.head=newnode 
            newnode.next=self.head #* 
        else : 
            curr=self.head 
            while curr.next is not self.head :
                curr=curr.next
            curr.next=newnode 
            newnode.next=self.head 

    def traverse(self) : 
            if not self.head : return [] 
    
            result=[]
            curr=self.head 
            while True :
                result.append(curr.data)
                curr=curr.next 
                if curr==self.head : 
                    break 
            return result

    def display(self) : 
        if not self.head : 
            return "No Cll"

        result=[]
        curr=self.head 
        while True :
            result.append(curr.data)
            curr=curr.next 
            if curr==self.head : 
                break 
        return result 
     
    def __str__(self):
        nodes = self.traverse()
        return " → ".join(map(str, nodes)) + " → (back to head)"

c=cll()
c.append(10)
c.append(20)
c.append(30)
print(c.display())
print(c)

