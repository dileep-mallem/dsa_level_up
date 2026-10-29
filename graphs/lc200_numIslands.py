from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # type: ignore
        # No of Connected Components , eight Directions , 
        # We take another grid as visited
        n=len(grid)
        m=len(grid[0])

        visited=[[False]*m for _ in range(n)]
        count=0

        def bfs(start_row, start_col, grid): 
            # Use unique names (start_row, start_col) to avoid variable shadowing
            visited[start_row][start_col] = True 
            q = deque([(start_row, start_col)])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while q :
                curr_row,curr_col = q.popleft()

                for dr, dc in directions: 
                    nr, nc = curr_row + dr, curr_col + dc 
                    if 0 <= nr < n and 0 <= nc < m: # check boundaries
                        if grid[nr][nc]=="1" and not visited[nr][nc] :  # if it's land, and unvisited
                            visited[nr][nc]=True
                            q.append((nr,nc))
        for r in range(n) : 
            for c in range(m) : 
                if grid[r][c]=="1" and not visited[r][c] : # LC passes the grid as an array of strings, not integer
                    bfs(r,c,grid)
                    count+=1

        return count 