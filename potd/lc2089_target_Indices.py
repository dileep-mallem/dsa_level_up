class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result=[]

        nums.sort()

        for i,v in enumerate(nums) : 
            if nums[i]==target :
                result.append(i)
        return result 
        