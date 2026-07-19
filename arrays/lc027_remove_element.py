#Pattern : Two Pointer

#Bit Tricky Question in aspect of its Language and Test Cases 
#One by one all Edge cases cleared 

# Time : O(n) Space : O(1) 

class Solution(object):
    def removeElement(self, nums, val):
        l,r=0,len(nums)-1
        for i in range(0,len(nums)):
            if l!=r : 
                if val == nums[l] :
                    if nums[r]!=val :
                        temp = nums[l]
                        nums[l]=nums[r]
                        nums[r]=temp 
                        r-=1
                    else :
                        while nums[r]==val and r > l :
                            r-=1
                        if r > l :
                            temp = nums[l]
                            nums[l]=nums[r]
                            nums[r]=temp
                            r-=1
                if r > l :
                    l+=1
        j=0
        for i in nums :
            if i!=val :
                j+=1
        return j 