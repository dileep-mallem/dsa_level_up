from collections import defaultdict , deque 


edges=[(1,2),(2,5),(5,7),(6,7),(6,3),(3,4),(3,1)]


adj_list=defaultdict(list)

for u,v in edges : 
    adj_list[u].append(v)
    adj_list[v].append(u)

print('Adj List for Given Graph \n',dict(adj_list),'\n') 

# Cycle Detection Using DFS 
visited=set()
def dfs(node : int , parent : int ) : 
    global visited
    global adj_list
    if node not in visited : 
        visited.add(node)

    for neighbour in adj_list[node] : 
        if neighbour not in visited : 
            visited.add(neighbour)
            if dfs(neighbour,node) : 
                return True 
        elif parent!=neighbour : # Cycle
            return True 
    return False 

print(f" Is there Any Cycle in graph : {dfs(1,-1)} ")
