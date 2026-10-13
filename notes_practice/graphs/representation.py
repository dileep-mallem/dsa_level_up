# (n,m) Graph , n-> Vertices m edges 
# Given (5,6) G -> edges 12,13,34,24,25,45

# Adj Matrix gor Given Graph 
# Space : adj[n][n] ->  n*n , and time : O(n**2)

edges = [(1,2), (4,2), (1,3), (3,4),(2,5),(4,5)] 
n,m=5,6
adj_mtx=[[0]*(n+1) for _ in range(n+1)]


for u,v in edges : 
    adj_mtx[u][v]=1
    adj_mtx[v][u]=1

print(adj_mtx)

\

#  Adjacency List Representation

# We use dict to repr adj.lists in pytho , 
# Space : O(n+m) 

from collections import defaultdict

adj_list=defaultdict(list)

# adj_list = [[] for _ in range(n + 1)]

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

print(adj_list) #  {1: [2, 3], 2: [1, 4, 5], 4: [2, 3, 5], 3: [1, 4], 5: [2, 4]})


# Explicit 
graph={}

for i in range(1,m) : 
    graph[i]=[]

for u, v in edges:
     graph[u].append(v)
     graph[v].append(u) 
print(graph)  # {1: [2, 3], 2: [1, 4, 5], 3: [1, 4], 4: [2, 3, 5], 5: [2, 4]}