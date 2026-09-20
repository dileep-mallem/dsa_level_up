import heapq 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq=Counter(nums)
        min_heap=[]

        for key,value in freq.items() : 
            
            heapq.heappush(min_heap,(value,key))
            # Push tuple of (freq,num) so heap sorts by freq
            
            if len(min_heap)> k :
                heapq.heappop(min_heap)

        return [key for value,key in min_heap]
