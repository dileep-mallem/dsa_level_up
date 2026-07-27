# HAshTables , Medium
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n=len(nums)
        # if n==1:
        #     return 0
    
        # max_length=0
        # sum=0
        # l=[]
        # i=0
        # while i < n :
        #     if nums[i]==0:
        #         if sum!=0 :
        #             sum-=1
        #             index_0=i
        #     else :
        #         sum=0
        #         index_1=i
        #     if nums[i]==1 :
        #         sum+=1
        #     l.append(sum)
        #     if sum in l :
        #         last_index=l.index(sum,)
        #         max_length=max(max_length,len(l[last_index+1:i]))
                
        # return max_length

        n = len(nums)
        balance_index = {0: -1}   # seed: balance 0 "occurred" before index 0
        balance = 0
        max_length = 0

        for i in range(n):
            balance += 1 if nums[i] == 1 else -1

            if balance in balance_index:
                max_length = max(max_length, i - balance_index[balance])
            else:
                balance_index[balance] = i   # only store the FIRST time we see this balance

        return max_length
        