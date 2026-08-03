class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Logic
        # result=[]
        # # for i in range(0,len(nums)): # TC :   > O(n2)
        # #     for j in range(0,len(nums)):
        # #         if (nums[i]+nums[j])==target and i!=j and i not in result and j not in result :
        # #             result.append(i)
        # #             result.append(j)
        # # return result

        # n=len(nums)
        # # for i in range(n) :
        # #     h[nums[i]] = i 
        # # O(n logn )
        # l=0
        # r=n-1
        # indexed = [(num,i) for i,num in enumerate(nums)]
        # indexed.sort()
        # while l < r : 
        #     sum = indexed[l][0] + indexed[r][0]
        #     if sum == target :
        #         return [indexed[l][1] , indexed[r][1]]
        #     elif sum > target :
        #         r-=1
        #     else :
        #         l+=1
       
      
        # O(n)
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i



