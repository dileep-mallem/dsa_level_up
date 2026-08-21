from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Precompute the LCM for all possible combinations of coins
        # along with the sign dictated by the Inclusion-Exclusion Principle.
        n = len(coins)
        lcm_subsets = []
        
        for r in range(1, n + 1):
            # Using alternating signs: add odd-sized subsets, subtract even-sized subsets
            sign = 1 if r % 2 == 1 else -1
            for comb in combinations(coins, r):
                # Calculate LCM for the current subset of coins
                curr_lcm = comb[0]
                for coin in comb[1:]:
                    curr_lcm = (curr_lcm * coin) // gcd(curr_lcm, coin)
                lcm_subsets.append((curr_lcm, sign))
        
        # Helper function to count how many valid amounts are <= x
        def count_amounts_less_or_equal(x: int) -> int:
            total_count = 0
            for lcm_val, sign in lcm_subsets:
                total_count += sign * (x // lcm_val)
            return total_count

        # Binary search range for the kth smallest amount
        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts_less_or_equal(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the amount boundary
                
        return ans

        
