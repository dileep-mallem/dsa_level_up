from collections import defaultdict
class Solution:
    def findNumberOfComponent(self, V, edges):
        visited=set()
        graph=defaultdict(list)
        # lets make Adj List 
        for i in range(1, V + 1):
            graph[i] = [] # Incase of Disconnected Nodes

        for u,v in edges : 
            graph[u].append(v)
            graph[v].append(u)

        # lets use dfs traversal 

        def dfs(graph , node : int  ) : 
            nonlocal visited 
            if node not in visited : 
                visited.add(node)
                print(node,end=" ")
            for neighbour in graph[node] : 
                if neighbour not in visited : 
                    dfs(graph,neighbour)

        # Finding Component 
        count=0 
        
        for i in range(1,V+1) : # lets take from one 
            if i not in visited : 
                dfs(graph,i)
                print()
                count+=1 
        return count 
    
s=Solution()
e=[(1,2),(1,3),(3,4),(2,4),(5,6),(6,7),(5,7),(8,9)]
print("Connected Components ")
ans=s.findNumberOfComponent(10,e)
print()
print("No of Connected Componets : " ,ans)
# Connected Components 
# 1 2 4 3 
# 5 6 7 
# 8 9 
# 10 

# No of Connected Componets :  4 