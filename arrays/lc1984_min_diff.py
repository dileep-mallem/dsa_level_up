import math
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minimum=math.inf
        for i in range(len(nums)-k+1):
            current_diff=nums[i+k-1]-nums[i] 
            if current_diff < minimum:
                minimum=current_diff
        return minimum 
