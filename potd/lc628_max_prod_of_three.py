class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==3 :
            return nums[0]*nums[1]*nums[2]

        nums.sort()
        max1 = nums[n-1]*nums[n-2]*nums[n-3]
        max2 = nums[0]*nums[1]*nums[n-1]

        return max(max1,max2)  