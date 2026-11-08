# First compute the column sums. Then sum the row sums that are larger than 1 or whose only 1 is in a column with more than one
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        cs = list(map(sum, zip(*grid)))
        return sum(
            rs
            for row in grid
            if (rs := sum(row))
            if rs > 1 or cs[row.index(1)] > 1
        )
