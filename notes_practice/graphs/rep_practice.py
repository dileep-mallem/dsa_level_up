# You're given a LeetCode-style input: n=5 nodes, edges=[[0,1],[1,2],[2,3],[3,4]]
# Write a function build_graph(n, edges, directed=False) that returns an adjacency list. 
# Handle directed and undirected cases.


from collections import defaultdict

n=5 
edges=[[0,1],[1,2],[2,3],[3,4]]

def build_graph(n,edges,directed=False) :
    adj_list=defaultdict(list)

    for u,v in edges : 
        adj_list[u].append(v)
        if directed==False : 
            adj_list[v].append(u)

    return adj_list 

undi=build_graph(n,edges)
di=build_graph(n,edges,True)
print(undi) # {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}) 
print(di) # 0: [1], 1: [2], 2: [3], 3: [4]})
 

