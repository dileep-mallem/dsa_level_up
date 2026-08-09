from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # suffix_sums[i] stores the total stones from pile i to the end
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        memo = {}
        
        def dfs(i, M):
            # If all piles are taken, no stones can be picked
            if i >= n:
                return 0
            # If a player can take all remaining piles, they should do it
            if i + 2 * M >= n:
                return suffix_sums[i]
            # Return cached result if already calculated
            if (i, M) in memo:
                return memo[(i, M)]
            
            # The current player tries to maximize their stones by minimizing 
            # the maximum stones the opponent can get from the remaining choice
            max_stones = 0
            for X in range(1, 2 * M + 1):
                opponent_stones = dfs(i + X, max(M, X))
                current_player_stones = suffix_sums[i] - opponent_stones
                max_stones = max(max_stones, current_player_stones)
                
            memo[(i, M)] = max_stones
            return max_stones
            
        return dfs(0, 1)