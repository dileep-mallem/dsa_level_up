import heapq
from collections import Counter 
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        
        freq=Counter(words)
        # min_heap=[]

        # for key,value in freq.items() : 
        #     heapq.heappush(min_heap,(value,key))

        #     if len(min_heap) > k :
        #         heapq.heappop(min_heap)
        # # l=[key for value,key in min_heap] # return lowest-> Highestt (Min_heap)


        # result = sorted(min_heap, key=lambda x: (-x[0], x[1]))
        # return [word for _, word in result]
        max_heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(max_heap)
        
        # Pull out the top k elements
        return [heapq.heappop(max_heap)[1] for _ in range(k)]

