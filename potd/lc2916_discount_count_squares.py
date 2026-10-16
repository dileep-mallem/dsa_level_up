class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum1 = [0] * (4 * n)  # Stores sum of d[i]
        self.sum2 = [0] * (4 * n)  # Stores sum of d[i]^2
        self.lazy = [0] * (4 * n)  # Lazy propagation array
        self.MOD = 10**9 + 7

    def _push_down(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        val = self.lazy[node]
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        # Update left child
        left_len = mid - start + 1
        self.sum2[left_child] = (self.sum2[left_child] + 2 * val * self.sum1[left_child] + val * val * left_len) % self.MOD
        self.sum1[left_child] = (self.sum1[left_child] + val * left_len) % self.MOD
        self.lazy[left_child] += val

        # Update right child
        right_len = end - mid
        self.sum2[right_child] = (self.sum2[right_child] + 2 * val * self.sum1[right_child] + val * val * right_len) % self.MOD
        self.sum1[right_child] = (self.sum1[right_child] + val * right_len) % self.MOD
        self.lazy[right_child] += val

        self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            length = end - start + 1
            self.sum2[node] = (self.sum2[node] + 2 * val * self.sum1[node] + val * val * length) % self.MOD
            self.sum1[node] = (self.sum1[node] + val * length) % self.MOD
            self.lazy[node] += val
            return

        self._push_down(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            # FIXED: The range for the right child must start at mid + 1
            self.update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.sum1[node] = (self.sum1[2 * node] + self.sum1[2 * node + 1]) % self.MOD
        self.sum2[node] = (self.sum2[2 * node] + self.sum2[2 * node + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        tree = SegmentTree(n)
        
        last_seen = {}
        total_ans = 0
        
        for j in range(n):
            last_idx = last_seen.get(nums[j], -1)
            
            # Increment distinct counts for all valid starting indices
            tree.update(1, 0, n - 1, last_idx + 1, j, 1)
            
            # tree.sum2[1] holds the sum of squares for the entire active array [0...j]
            total_ans = (total_ans + tree.sum2[1]) % MOD
            
            last_seen[nums[j]] = j
            
        return total_ans