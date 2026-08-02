class Solution(object):
    def runningSum(self, nums):
        l=[]
        for i in range(len(nums)):
            if l :
                l.append(l[-1]+nums[i])
            else :
                l.append(nums[i])
        return l