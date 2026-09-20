import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        
        # For k + largest -> minHEap , top -> min
        # for k + smallst -> maxHeap , top -> max 

        
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
       
        for i in range(k, len(nums)):
            
            if nums[i] > min_heap[0]:
               
                heapq.heappushpop(min_heap, nums[i])
                
        # The root of the heap is the k-th largest element
        return min_heap[0]
