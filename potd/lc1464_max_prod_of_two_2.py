class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        i=n-1
        j=n-2

        return (nums[i]-1) * (nums[j]-1)