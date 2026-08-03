class Solution(object) : 
    def numberOfSteps(self,n) :
        # if n is even , divide by 2 .Otherwise subtract by 1 
        def steps(num,st) : 
            if num==0 : 
                return st 
            if num%2==0 : 
                return steps(num//2,st+1)
            else :
                return steps(num-1,st+1)
        x=steps(n,0) # Initial 
        return x

s=Solution()
print(s.numberOfSteps(14))