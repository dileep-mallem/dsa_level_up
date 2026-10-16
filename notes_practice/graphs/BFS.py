from collections import defaultdict,deque

edges=[(1,2),(1,6),(2,4),(2,3),(6,7),(6,8),(4,5),(5,7)]

# Build Adj Lists 

adj_list=defaultdict(list)

for u,v in edges : 
    adj_list[u].append(v)
    adj_list[v].append(u)

print(" Adjacent List of given graph ",dict(adj_list)) # convert to reg =dict 
# Python's defaultdict is a specialized subclass of the standard dictionary (dict).
# When you print an object directly in Python, it uses its built-in representation method (called __repr__) to show you exactly what type of object it is, along with its contents.

# BFS Traversal  : Explores Level by level 
# Start at source , visit al immediates neightbius first , then their neightbous and so on .
# Use a queue(FIFO) 
# guaratess shortest path in unweighted graphs 

def bfs(graph : dict , start : int) -> list : 
    visited={start} # SET — O(1) lookup, not a list

    queue=deque([start]) # deque — O(1) popleft, not list.pop(0) 
    order=[]

    while queue : 
        node=queue.popleft() # FIFO
        order.append(node)

        for neighbour in graph[node] : 
            if neighbour not in visited : 
                visited.add(neighbour)
                queue.append(neighbour)
    return order

print(" \n BFS Traveral ")
print(f" Starting Node 1 : {bfs(adj_list,1)}") # [1, 2, 6, 4, 3, 7, 8, 5] 
print(" Starting Node 6 : ",bfs(adj_list,6)) #  [6, 1, 7, 8, 2, 5, 4, 3]









