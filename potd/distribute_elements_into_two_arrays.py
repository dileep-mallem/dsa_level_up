class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        arr1,arr2=[],[]
        for i in range(len(nums)) :
            if (i+1)==1 :
                arr1.append(nums[i])
            elif (i+1)==2:
                arr2.append(nums[i])
            else :
                if arr1[-1] > arr2[-1] :
                    arr1.append(nums[i])
                else :
                    arr2.append(nums[i])

        return arr1+arr2
