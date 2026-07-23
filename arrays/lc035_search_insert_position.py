#Topic : Arrays , Easy 
#TC : O(log n) , 
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums :
            return nums.index(target)
        else : #if its not Found 
            if target < nums[0] :
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
            else :
                for i in range(0,len(nums)-1): # We write Both Edge Case at top so Thier TC is O(1) which results TC of this loop be O(log n)
                    if nums[i] < target < nums[i+1]:
                        return i+1 
                    