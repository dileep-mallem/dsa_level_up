import heapq 


# Buling a heap 
h=[5,1,8,3,2]
heapq.heapify(h) # tranform in place ->] , O(n)
print("Heap : ",h) #  [1,2,8,3,5

# Push and Pop 
heapq.heappush(h,0) # push 0 → O(log n)
print("Heap : ",h) # Heap :  [0, 2, 1, 3, 5, 8]
print(h[0]) # 0 -> peek min , O(1)

x=heapq.heappop(h) # Remove adn Return min -> O(log n)
print(x) # 0
print("Heap : ",h)


# pushpop and replace 
heapq.heappushpop(h,4) # Push then pop , faster than push+pop
heapq.heapreplace(h,4) # pop then push ,faster than pop+push

# nlargest/nsmallest -> convienence functions
nums=[3,1,4,1,5,9,2,6]
heapq.nlargest(3,nums) # [9,6,5] -> top 3 largest 
heapq.nsmallest(3,nums) # [1,1,2] -> top3 smallest 
# Use these only for small k , for large k, sorted() is faster
nums=[3,2,1,5,6,4]
heapq.heapify(nums)
print(nums)
x=heapq.nlargest(2,nums)
print(x)




# max heap : negate Values 
maxheap=[]
for v in [5,1,8,3] : 
    heapq.heappush(maxheap,-v) # negate to invert order 
max_val=-heapq.heappop(maxheap) # 8 -> negate back 

# Heap of tuples — for priority queues
# heapq compares tuples element by element

task_queue=[]

heapq.heappush(task_queue,(1,"low priority task"))
heapq.heappush(task_queue,(0,"urgent task"))
heapq.heappush(task_queue,(2,"background task"))
print(task_queue) # [(0, 'urgent task'), (1, 'low priority task'), (2, 'background task')]
priority,task=heapq.heappop(task_queue)
print(priority,task)  # 0 urgent task


class MinHeap:
    def __init__(self): 
        self.h = []
    def push(self, val):  
        heapq.heappush(self.h, val)
    def pop(self):       
        return heapq.heappop(self.h)
    def peek(self):     
        return self.h[0]
    def __len__(self):   
        return len(self.h)
    
    def __bool__(self):  
        return bool(self.h)

class MaxHeap:
    def __init__(self): 
        self.h = []
    def push(self, val):  
        heapq.heappush(self.h, -val)
    def pop(self):       
        return -heapq.heappop(self.h)
    def peek(self):      
        return -self.h[0]
    def __len__(self):   
        return len(self.h)