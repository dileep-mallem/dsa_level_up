from collections import deque

class Solution:
    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        visited = set()
        
        # Helper function to detect cycle in a single connected component using BFS
        def detect(source: int) -> bool:
            visited.add(source)
            q = deque([(source, -1)])  # (current_node, parent_node)
            
            while q:
                node, parent = q.popleft()
                
                for neighbour in adj[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append((neighbour, node))
                    elif parent != neighbour: 
                        # Neighbor is visited and is NOT the parent -> Cycle detected
                        return True
            return False
            
        # Loop through all vertices to handle disconnected graph components
        for i in range(V):
            if i not in visited:
                if detect(i):
                    return True
                    
        return False
