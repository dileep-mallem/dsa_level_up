class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here
        # Sliding Wnidow
        
        n=len(arr) 
        
        if n < k :
            return 0
        # Step 1: Compute max subarray sum ending at each index using Kadane's
        max_ending_here = [0] * n
        current_max = 0
        
        for i in range(n):
            current_max = max(arr[i], current_max + arr[i])
            max_ending_here[i] = current_max
        

        current_sum=sum(arr[:k])
        max_sum = current_sum
        
        for j in range(k,n):
            
            current_sum +=  arr[j] - arr[j-k]
            
            if current_sum>max_sum :
                max_sum=current_sum 
             # Check if adding the best subarray ending just before this window helps
            max_sum = max(max_sum, current_sum + max_ending_here[j - k])
            
      
        return max_sum
            