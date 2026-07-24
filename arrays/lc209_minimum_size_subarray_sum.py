#Topic : Sliding Window (Dynamic) 
# Difficulty : MEd 
# Tc ; O(n2) 

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # l and r , both starts from 0 index 
        # if sum >= target -> l+=1 (shrinks) , sum < target -> r+=1 
        # min_length=min(min_length,r-l+1) 
        # code stops when l > r 
        n = len(nums)

        l = 0
        total = 0
        min_length = float('inf')

        for r in range(n):

            total += nums[r]          # Expand the window

            while total >= target:    # Shrink the window
                min_length = min(min_length, r - l + 1)

                total -= nums[l]
                l += 1

        if min_length == float('inf'):
            return 0

        return min_length