#Reevist When Graphs are happening
from collections import deque
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build the graph representation
        graph = {i: [] for i in range(n)}
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 2: Identify all suspicious methods via BFS
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # An external method relies on a suspicious method; cannot remove anything
                return list(range(n))
                
        # Step 4: Safely return only the remaining non-suspicious methods
        return [i for i in range(n) if i not in suspicious]