# Revists , Dps , Hard , return True us also Answer(Both oaly Optimally) but this is by understanding 
class Solution(object):
    def stoneGameIII(self, stoneValue):
        
        n = len(stoneValue)
        # Using 4 elements to optimize space instead of a full size n+1 array
        dp = [0] * 4
        
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp[(i + 1) % 4]
            
            take2 = float('-inf')
            if i + 1 < n:
                take2 = stoneValue[i] + stoneValue[i + 1] - dp[(i + 2) % 4]
                
            take3 = float('-inf')
            if i + 2 < n:
                take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[(i + 3) % 4]
                
            dp[i % 4] = max(take1, take2, take3)
            
        alice_margin = dp[0]
        
        if alice_margin > 0:
            return "Alice"
        elif alice_margin < 0:
            return "Bob"
        return "Tie"