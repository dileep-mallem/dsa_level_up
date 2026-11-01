class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # There are n elements, after reordering, the minimum element is a(1), the maximum element is a(n), we have a(1) <= a(2) <= a(3) <= ... <= a(n).
        # We set the solution is m, after m moves, all the elements will be the same value, that is a(1) + m, so the other (n-1) element will add a(1) + m - a(i) times, we know that m moves will introduce m * (n - 1) to the array's total sums. we can have the equation:
        # m * (n - 1) = m + a(1) + m - a(2) + a(1) + m - a(3) +... + a(1) + m - a(n)
        # => m * n - m = m * n + (n - 1) * a(1) - a(2) - a(3) -... - a(n)
        # => m = a(2) + a(3) + ... + a(n) - (n - 1) * a(1)
        # => m = Sum - n * Min

        # Done!
        n=len(nums)
         

        return sum(nums) - n * min(nums)