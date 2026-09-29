from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 1. An odd length path can never be balanced
        if (m + n - 1) % 2 != 0:
            return False
        
        # 2. Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        @lru_cache(None)
        def dfs(i: int, j: int, balance: int) -> bool:
            # Update balance based on the current cell content
            balance += 1 if grid[i][j] == '(' else -1
            
            # Pruning Condition 1: Too many closed parentheses
            if balance < 0:
                return False
                
            # Pruning Condition 2: Remaining steps cannot close the open parentheses
            remaining_steps = (m - 1 - i) + (n - 1 - j)
            if balance > remaining_steps:
                return False
                
            # Base Case: Reached the destination
            if i == m - 1 and j == n - 1:
                return balance == 0
                
            # Try moving down and right
            res = False
            if i + 1 < m:
                res = res or dfs(i + 1, j, balance)
            if j + 1 < n:
                res = res or dfs(i, j + 1, balance)
                
            return res

        return dfs(0, 0, 0)
