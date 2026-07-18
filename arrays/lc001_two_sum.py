#First didn't thougt og=f not in and i!=j ,so repetetion Occurs

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Logic
        result=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (nums[i]+nums[j])==target and i!=j and i not in result and j not in result :
                    result.append(i)
                    result.append(j)
        return result
                