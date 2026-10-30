import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int: # type: ignore
        # n verrtices in directed weighted graph from 0 to n-1 
        #  edges[i] = [ui, vi, wi]

        #  minimum total edge weight of a path from node 0 to node n - 1 
        #  Dijkstra's algorithm with an expanded state

        # adj list creation 
        g=[[] for _ in range(n)]
        for x,y,w in edges :
            g[x].append((y,w))

        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
        # {shortest path length, node index, number of consecutive identical letters at the end} 

        pq=[]

        dis[0][1]=0

        heapq.heappush(pq,(0,0,1))

        while  pq : 
            d,x,cnt=heapq.heappop(pq)

            if d > dis[x][cnt] : 
                continue 
            if x==n-1 :
                return d 
            for y,w in g[x]:
                new_cnt=cnt + 1 if labels[x]==labels[y] else 1 
                if new_cnt > k :
                    continue 
                nd=d+w 
                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt]=nd 
                    heapq.heappush(pq,(nd,y,new_cnt))
        return -1