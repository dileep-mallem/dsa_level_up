from collections import defaultdict , deque 


edges=[(1,2),(2,5),(5,7),(6,7),(6,3),(3,4),(3,1)]

adj_list=defaultdict(list)

for u,v in edges : 
    adj_list[u].append(v)
    adj_list[v].append(u)

print('Adj List for Given Graph \n',dict(adj_list),'\n')


# Detecting Cycle in Undi Graph using BFS 


def detect(source : int , adj : dict , visited : set | None ) :

    if visited is None : 
        visited=set() 
    visited.add(source)

    q=deque([(source,-1)]) # Initial 

    while q : 
        node,parent=q.popleft()

        for neighbour in adj[node]: 
            if neighbour not in visited : 
                visited.add(neighbour)
                q.append((neighbour,node))
            elif parent!=neighbour : # if it is Visited and it did not come from it , means it is not parent and it is a cycle 
                return True 
    return False 

print(f" Is there Any Cycle in graph : {detect(1,adj_list,None)} ")


# If there are Connected Components 

edge=[(1,2),(2,4),(1,3),(5,6),(7,8),(8,9),(7,9)]
conn_adj=defaultdict(list)
n=9
for i in range(1,10) : 
    conn_adj[i]=[] # Incase of Dissconnets 
for u,v in edge : 
    conn_adj[u].append(v)
    conn_adj[v].append(u)
print('Adj List for Given Connected Compomnents  \n',dict(conn_adj),'\n')
            
# We need Once for each Component 
def conn_cycle(n : int , graph : dict ) : 
    visited=set()
    for i in range(1,n+1) : 
        if i not in visited : 
            if detect(i,graph,None) : 
                return True 
    return False 


print(f" Is there Any Cycle in graph : {conn_cycle(9,conn_adj)} ") # True 

        

     



