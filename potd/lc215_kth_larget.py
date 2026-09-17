import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums) # nums -> minHeap 
        x=heapq.nlargest(k,nums)

        return x[k-1]