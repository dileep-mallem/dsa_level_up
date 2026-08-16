class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
         # Step 1: Count occurrences of each remainder
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1
            
        # Step 2: Evaluate the game based on the parity of type-0 stones
        if count[0] % 2 == 0:
            return min(count[1], count[2]) > 0
        
        return abs(count[1] - count[2]) > 2