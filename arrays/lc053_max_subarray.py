# Topic : Kadanes Algo , Easy 
# TC : O(n) , sc : O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max=nums[0]
        global_max=nums[0]

        n=len(nums)
        # if n == 1 :
        #     return nums[0]
        
        for i in range(1,n):
            current_max=max(nums[i],current_max+nums[i])
            global_max=max(global_max,current_max)

        return global_max if n > 1 else nums[0]