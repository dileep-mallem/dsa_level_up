class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        
        arr.sort()
        # count of triplets of sum <=r - sum<=l-1 
        
        def Count(nums , x ) :
            n = len(nums)
            count = 0
            for i in range(n - 2):
                left = i+1
                right = n-1
                
                
                while left < right:
                    current_sum = nums[i] + nums[left] + nums[right]
                    
                    if current_sum <= x:
                        # If current_sum <= x, then all elements from left to right 
                        # will also form  valid triplet i and left 
                        count += (right - left)
                        left += 1  # Move left pointer forward to increase the sum
                    else:
                        right -= 1 # Move right pointer backward to decrease the sum
            return count
            
        return Count(arr,r) - Count(arr,l-1)