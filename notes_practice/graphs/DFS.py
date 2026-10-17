# DFS : Depth First Search , Uses Stack(expicit or call via recursion) 
# Explores as far as possible 
# Visita all reachable nodes but not necessarily in shortest - path order 

from collections import defaultdict

edges=[(1,2),(1,3),(2,5),(2,6),(8,7),(4,8),(4,3),(3,7)]


adj_list=defaultdict(list)

for u,v in edges : 
    adj_list[u].append(v)
    adj_list[v].append(u)


def dfs_recursive(graph : dict , node : int , visited : set | None = None) : 
    if visited is None : 
        visited=set()

    visited.add(node)
    print(node,end=",") # pricess the node 

    for neighbour in graph.get(node,[]) : 
        if neighbour not in visited : 
            dfs_recursive(graph,neighbour,visited) 
print(" DFS recursive")
print("\n Starting Node 1 :")
dfs_recursive(adj_list,1)
print("\n Starting Node 3 :")
dfs_recursive(adj_list,3)

# Iterativs DFS 
def dfs_iterative(graph : dict , start : int) : 
    visited=set()
    stack=[start]

    while stack : 
        node=stack.pop()

        if node not in visited : 
            visited.add(node)
            print(node,end=",")

            for neighbour in reversed(graph.get(node,[])) : 
                if neighbour not in visited : 
                    stack.append(neighbour)
print("\n\n Iterative DFS")
print(" Starting Node 1 :")
dfs_iterative(adj_list,1)
print("\n Starting Node 3 :")
dfs_iterative(adj_list,3)
print()
   




