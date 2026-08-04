#Easy , O(n) , Try with HashTables 
class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        n=len(nums)
        # k=0
        l=[]
        # for i in range(1,n):
        #     while nums[k]+1 != nums[i] :
        #         l.append(nums[k]+1)
        #         nums[k]=nums[k]+1
        #     k=i
        # return l

        # Using Hash Tables 