class Solution:
    def mySqrt(self, x: int) -> int:

        # def root(x) : # O(root(n))
        #     result=0
        #     # space : [0,x//2]
        #     k=0

        #     if k > x//2 :
        #         return result
        #     while k*k<= x :
        #         result=k
        #         k+=1 
        #     return result
        # return root(x)

        if x < 2 :
            return x 
        left,right=0,x//2 

        while left <=right :
            mid = left + (right - left) // 2
            square = mid * mid 
            if square==x :
                return mid
            elif square < x :
                left=mid+1
            else :
                right=mid-1
        # 'right' will hold the truncated integer floor value
        return right
