class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # dp[i] stores the minimum length of sub-array with sum == target in arr[0...i]
        dp = [float('inf')] * n
        prefix_sums = {0: -1}
        current_sum = 0
        min_len_so_far = float('inf')
        ans = float('inf')

        for i in range(n):
            current_sum += arr[i]
            # Check if (current_sum - target) exists in prefix sums
            if (current_sum - target) in prefix_sums:
                start = prefix_sums[current_sum - target]
                current_len = i - start

                # If there is a valid non-overlapping sub-array before 'start'
                if start >= 0 and dp[start] != float('inf'):
                    ans = min(ans, current_len + dp[start])

                # Update min_len_so_far with current sub-array length
                min_len_so_far = min(min_len_so_far, current_len)

            dp[i] = min_len_so_far
            prefix_sums[current_sum] = i

        return ans if ans != float('inf') else -1