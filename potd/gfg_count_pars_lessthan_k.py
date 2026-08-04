class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        arr.sort()
        n=len(arr)
        
        count=0
        
        l=0
        for r in range(n) :
            while arr[r] - arr[l] >=k :
                l+=1
                
            count += (r-l)
        return count