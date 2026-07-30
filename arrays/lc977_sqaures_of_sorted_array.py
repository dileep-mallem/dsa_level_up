# Easy
class Solution(object):
    def sortedSquares(self, nums):
        # sqaure each element nd sort () O(n)
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # nums.sort()
        # return nums

        # USing Two pointers O(n)
        n=len(nums)
        result=[0]*n
        l=0
        r=n-1
        k=n-1

        while l <=r :
            x=max(abs(nums[l]),abs(nums[r]))

            if x==abs(nums[l]):
                result[k]= nums[l]*nums[l]
                l+=1 
            else :
                result[k]= nums[r]*nums[r]
                r-=1
            k-=1
        return result
