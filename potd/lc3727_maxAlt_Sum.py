class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        absoluteArr=[]
        n=len(nums)

        for num in nums : 
            absoluteArr.append(abs(num))
           
        # Asc and Dec order arrays 
        
        asc=sorted(absoluteArr)
        dsc=asc[::-1]

        result1=0
        l1=0
        l2=0
        result2=0
        for i in range(n) :
            if i%2==0 :
                result1 += dsc[l1]**2 
                l1+=1
            else :
                result2 += asc[l2]**2 
                l2+=1
        return result1-result2
            