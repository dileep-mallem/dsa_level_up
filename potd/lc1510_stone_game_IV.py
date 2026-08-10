class Solution:
    def winnerSquareGame(self, n: int) -> bool:
         # dp[i] represents if the player whose turn it is can win with 'i' stones left
        dp = [False] * (n + 1)
        
        # Iteratively calculate winning states from 1 to n stones
        for i in range(1, n + 1):
            k = 1
            # Try removing every possible perfect square less than or equal to i
            while k * k <= i:
                # If removing k*k stones forces the opponent into a losing state, we win
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # No need to check other moves for this stone count
                k += 1
                
        return dp[n]