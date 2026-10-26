class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int: # type: ignore

        rows=len(grid)
        cols=len(grid[0]) 

        count=0
        total=0 

        def dfs(r,c) : 
            nonlocal total 

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 
            
            # Add cell value and mark it visited to avoid revisiting 

            if grid[r][c]==0 :
                return 

            
            total+=grid[r][c]
            grid[r][c]=0 
           
             

            # Explore all diff cells 

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # Explore each island and count it if its sum is divisible by k 
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c]!=0 :
                    total=0 
                    dfs(r,c)
                    if total %k==0 :
                        count+=1 
                  
        
        return count 