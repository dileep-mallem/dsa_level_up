from collections import defaultdict 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: # type: ignore
        visited=set()
        graph=defaultdict(list)
        # lets make Adj List 
        n=len(isConnected)
        for i in range(1, n + 1):
            graph[i] = []
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].append(j+1)
        # lets use dfs traversal 

        def dfs(graph , node : int  ) : 
            nonlocal visited 
            if node not in visited : 
                visited.add(node)
            for neighbour in graph[node] : 
                if neighbour not in visited : 
                    dfs(graph,neighbour)

        # Finding Component 
        count=0 
        
        for i in range(1,n+1) : # lets take from one 
            if i not in visited : 
                dfs(graph,i)
                count+=1 
        return count