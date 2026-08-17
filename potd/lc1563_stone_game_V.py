class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        from typing import List

        n = len(stoneValue)
        if n == 1:
            return 0
            
        # Prefix sum for O(1) interval sum calculations
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        # dp[i][j] = maximum score Alice can get from range [i, j]
        dp = [[0] * n for _ in range(n)]
        
        # max_left[i][j] caches max(dp[i][k] + sum(i, k)) for k from i to j
        max_left = [[0] * n for _ in range(n)]
        # max_right[i][j] caches max(dp[k+1][j] + sum(k+1, j)) for k from i to j
        max_right = [[0] * n for _ in range(n)]

        # Initialize base cases for single element intervals
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]

        # Maintain a sliding mid pointer for each starting position i
        mid_pt = [i for i in range(n)]

        # Bottom-up Tabulation by interval length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Advance mid pointer until left_sum >= right_sum
                while (pref[mid_pt[i] + 1] - pref[i]) < (pref[j + 1] - pref[mid_pt[i] + 1]):
                    mid_pt[i] += 1
                    
                mid = mid_pt[i]
                
                # Case 1: k is in [i, mid - 1] -> left_sum < right_sum
                # Bob discards right. We fetch the maximum possible score directly in O(1)
                res1 = max_left[i][mid - 1] if mid - 1 >= i else 0
                
                # Case 2: k is in [mid + 1, j - 1] -> left_sum > right_sum
                # Bob discards left. We fetch the precalculated max right score in O(1)
                res2 = max_right[mid + 1][j] if mid + 1 <= j else 0
                
                # Boundary check: If left_sum == right_sum precisely at k = mid
                if (pref[mid + 1] - pref[i]) == (pref[j + 1] - pref[mid + 1]):
                    res2 = max(res2, dp[i][mid] + (pref[mid + 1] - pref[i]))
                
                # Store the optimal score for the current interval
                dp[i][j] = max(res1, res2)
                
                # Update prefix and suffix helper caches for subsequent rounds
                current_total = dp[i][j] + (pref[j + 1] - pref[i])
                max_left[i][j] = max(max_left[i][j - 1], current_total)
                max_right[i][j] = max(max_right[i + 1][j], current_total)

        return dp[0][n - 1]